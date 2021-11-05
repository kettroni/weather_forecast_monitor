from typing import List
import aiohttp
import asyncio
import requests
from models.abc_classes import APIFetcher
from models.weather_data import WeatherData
from models.config_classes import APIFetcherConfiguration


class OpenweatherFetcher(APIFetcher):
    def __init__(self, api_fetcher_config: APIFetcherConfiguration):
        self.config = api_fetcher_config
        self.api_key = self.config.api_key
        self.api_urls = self._create_urls()

    async def get_weather_data(self) -> List[WeatherData]:

        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.api_urls:
                task = asyncio.ensure_future(self.get_one_weather_data(session, url))
                tasks.append(task)

            results = await asyncio.gather(*tasks)

        return results

    async def get_one_weather_data(
        self, session: aiohttp.ClientSession, url: str
    ) -> WeatherData:
        async with session.get(url) as res:
            weather_data = await res.json()
            return weather_data

    def _valid_result(self, result: requests.Response):
        if result.status_code == 200:
            return True
        else:
            return False

    def _create_urls(self) -> List[str]:
        locations = self.config.locations
        api_urls = []
        for location in locations:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.lat}&lon={location.lon}&appid={self.api_key}"
            api_urls.append(url)
        return api_urls
