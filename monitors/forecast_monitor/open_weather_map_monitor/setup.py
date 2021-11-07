from utils.load_config import load_api_fetcher_config
from .openweather_fetcher import OpenweatherFetcher
from .our_api_sender import OurApiSender


def get_fetcher():
    api_fetcher_config = load_api_fetcher_config("./monitors/forecast_monitor/open_weather_map_monitor/fetcher_config.yaml")
    return OpenweatherFetcher(api_fetcher_config)


def get_sender():
    return OurApiSender("http://127.0.0.1:5000/forecasts")

