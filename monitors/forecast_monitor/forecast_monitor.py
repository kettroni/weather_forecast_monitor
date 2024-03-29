"""
This is a general implementation of a ForecastMonitor.
Pass instances of an APIFetcher and an APISender (abstractions are defined in models/abstracts/)
for this class and it should work.
"""
from logging import Logger
import time
import asyncio
from datetime import datetime
from typing import List
import aiohttp
from models.config_classes import MonitorConfiguration
from models.abstracts import (
    Monitor,
    APIFetcher,
    APISender,
    APIFetcherError,
    APISenderError,
)
from models.data import ForecastData, WeatherData, MonitorData


class ForecastMonitor(Monitor):
    def __init__(
        self,
        monitor_config: MonitorConfiguration,
        api_fetcher: APIFetcher,
        api_sender: APISender,
        logger: Logger,
    ):
        self.monitor_config = monitor_config
        self.api_fetcher = api_fetcher
        self.api_sender = api_sender
        self.logger = logger
        self.loop = 0

    def run(self):
        # Try block for running the monitor, closes monitor with KeyboardInterrupt.
        try:
            # Try block for handling different kinds of errors.
            try:
                while True:
                    # Run the monitor loop and start another after checking_frequency.
                    asyncio.run(self._monitor_loop())
                    time.sleep(self.monitor_config.checking_frequency)
            except APIFetcherError as err:
                self.logger.error(err)
                self._restart_after_seconds(5)
            except APISenderError as err:
                self.logger.error(err)
                self._restart_after_seconds(5)
            except Exception as err:
                self.logger.exception(f"Unexpected error faced: {err}")

        except KeyboardInterrupt:
            self.logger.info("Shutting down the monitor...")

    async def _monitor_loop(self):
        self.loop += 1
        loop = self.loop
        self.logger.info(f"Loop #{loop} started.")

        for monitor_data in self.monitor_config.monitor_datas:
            location = monitor_data.location

            self.logger.info(f"[#{loop}] Fetching WeatherData for location {location}")
            weather_data = await self.api_fetcher.get_weather_data(location)

            # Handle the fetched WeatherData and get ForecastData
            forecast_data = self._handle_weather_data(monitor_data, weather_data)

            # Log the results (ForecastData)
            self._result_logging(monitor_data, forecast_data, loop)

            # Update database with api_sender
            status_code = await self.api_sender.send_forecast_data(forecast_data)
            if status_code == 201:
                self.logger.info(f"[#{loop}] Database updated succesfully!")
            else:
                self.logger.error(f"[#{loop}] Database was not updated correctly.")

        self.logger.info(f"Loop #{loop} finished.")

    def _handle_weather_data(
        self, monitor_data: MonitorData, weather_data: WeatherData
    ) -> ForecastData:
        temperature_exceeded = False

        for unit in weather_data.units:
            if unit.temp_max > monitor_data.temp_limit.high_temp:
                temperature_exceeded = True
            if unit.temp_min < monitor_data.temp_limit.low_temp:
                temperature_exceeded = True

        forecast_data = ForecastData(
            lat=weather_data.lat,
            lon=weather_data.lon,
            low_temp=monitor_data.temp_limit.low_temp,
            high_temp=monitor_data.temp_limit.high_temp,
            exceeds_limits=temperature_exceeded,
            timestamp=datetime.now().strftime("%d-%m-%y_%H:%M:%S"),
        )

        return forecast_data

    def _result_logging(
        self, monitor_data: MonitorData, forecast_data: ForecastData, loop: int
    ) -> None:
        temp_limit = monitor_data.temp_limit
        location = monitor_data.location
        if forecast_data.exceeds_limits:
            self.logger.warning(
                f"[#{loop}] Temperature limits {str(temp_limit)}  EXCEEDED in the next 5 days for {location}."
            )
        else:
            self.logger.info(
                f"[#{loop}] Temperature limits were NOT exceeded in the next 5 days for {location}"
            )

    def _restart_after_seconds(self, seconds: int):
        self.logger.info(f"Restarting after {seconds} seconds...")
        time.sleep(seconds)
        self.loop = 0
        self.run()
