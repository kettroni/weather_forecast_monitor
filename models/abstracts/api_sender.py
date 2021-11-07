from abc import ABC, abstractmethod
from models.data import ForecastData


class APISender(ABC):
    @abstractmethod
    async def send_forecast_data(self, data: ForecastData) -> int:
        """
        Send forecast data to an API and return a status code
        that indicates if the saving of the data was succesfull or not.
        """


class APISenderError(Exception):
    pass
