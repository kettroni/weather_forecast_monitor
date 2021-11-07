from abc import ABC, abstractmethod
from models.data import WeatherData, Location


class APIFetcher(ABC):
    @abstractmethod
    async def get_weather_data(self, location: Location) -> WeatherData:
        """
        Get WeatherData by using a location.
        """
        pass


class APIFetcherError(Exception):
    pass
