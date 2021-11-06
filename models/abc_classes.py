import asyncio
from abc import ABC, abstractmethod
from typing import List
from models.weather_data import WeatherData
from models.forecast_data import ForecastData
from models.config_classes import MonitorConfiguration
from models.location import Location


class APIFetcher(ABC):
    @abstractmethod
    def get_weather_data(self) -> WeatherData:
        pass

    @abstractmethod
    def _create_url(self) -> str:
        pass


class APISender(ABC):
    @abstractmethod
    def send_forecast_data(self, data: ForecastData) -> None:
        pass


class Monitor(ABC):
    @abstractmethod
    def run(self):
        pass


class APIFetcherError(Exception):
    pass


class APISenderError(Exception):
    pass
