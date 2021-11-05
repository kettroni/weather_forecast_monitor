import asyncio
from abc import ABC, abstractmethod
from typing import List
from models.weather_data import WeatherData
from models.forecast_data import ForecastData
from models.config_classes import MonitorConfiguration


class APIFetcher(ABC):
    @abstractmethod
    def get_weather_data(self) -> List[WeatherData]:
        pass


class APISender(ABC):
    @abstractmethod
    def send_forecast_data(self, data: ForecastData) -> None:
        pass


class Monitor(ABC):
    @abstractmethod
    def run(self):
        pass
