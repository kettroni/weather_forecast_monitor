from models.abc_classes import APIFetcher
from models.weather_data import WeatherData


class OpenweatherFetcher(APIFetcher):
    def __init__(self, apikey: str):
        self.api_key = apikey

    def get_weather_data(self) -> WeatherData:
        return []

