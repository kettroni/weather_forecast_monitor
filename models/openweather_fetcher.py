from typing import List, Dict
import aiohttp
import asyncio
import requests
from models.abc_classes import APIFetcher
from models.weather_data import WeatherData, WeatherUnit
from models.config_classes import APIFetcherConfiguration
from models.location import Location


class OpenweatherFetcher(APIFetcher):
    def __init__(self, api_fetcher_config: APIFetcherConfiguration):
        self.config = api_fetcher_config
        self.api_key = self.config.api_key

    async def get_weather_data(self, location: Location) -> WeatherData:
        url = self._create_url(location)

        async with aiohttp.ClientSession() as session:
            task = asyncio.ensure_future(self.get_one_weather_data(session, url))
            res = await task
            weather_data = self._response_to_weather_data(res)

        return weather_data

    async def get_one_weather_data(
        self, session: aiohttp.ClientSession, url: str
    ) -> WeatherData:
        async with session.get(url) as res:
            weather_data = await res.json()

            return weather_data

    def _response_to_weather_data(self, res_json: Dict) -> WeatherData:
        try:
            weather_units = []
            for item in res_json["list"]:
                weather_unit = WeatherUnit(
                    temp_max=item["main"]["temp_max"],
                    temp_min=item["main"]["temp_min"],
                    dt_txt=item["dt_txt"],
                )
                weather_units.append(weather_unit)

            weather_data = WeatherData(
                lat=res_json["city"]["coord"]["lat"],
                lon=res_json["city"]["coord"]["lon"],
                units=weather_units,
            )

            return weather_data
        except KeyError as error:
            raise error

    def _create_url(self, location) -> str:
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.lat}&lon={location.lon}&appid={self.api_key}"
        return url


class FetcherError:
    pass
