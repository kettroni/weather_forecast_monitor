import asyncio
from models.abc_classes import APISender
from models.forecast_data import ForecastData


class OurApiSender(APISender):
    def send_forecast_data(self, data: ForecastData):
        return []

