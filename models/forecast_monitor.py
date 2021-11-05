from logging import Logger
import time
import asyncio
from typing import List
from models.config_classes import MonitorConfiguration
from models.abc_classes import Monitor, APIFetcher, APISender
from models.forecast_data import ForecastData
from models.weather_data import WeatherData




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
        self.threads = []

    def run(self):
        try:
            while True:
                asyncio.run(self._monitor_loop())
                time.sleep(self.monitor_config.checking_frequency)
        except KeyboardInterrupt:
            self.logger("Shutting down the monitor...")
        except Exception as err:
            self.logger.exception(f"Unexpected error faced:")
            self.logger.exception(err)


    async def _monitor_loop(self):
        self.logger.info("Fetching WeatherData")
        weather_data = await self.api_fetcher.get_weather_data()
        self.logger.info(f"Found: {weather_data}")

        self.logger.info("Transforming WeatherData -> ForecastData")
        forecast_data = self._transform(weather_data)
        self.logger.info(f"Transformed: {forecast_data}")

        self.logger.info("Sending ForecastData")
        self.api_sender.send_forecast_data(forecast_data)

        self.logger.info("Loop finished.")

    def _transform(self, weather_data: List[WeatherData]) -> List[ForecastData]:
        return []
