from typing import List, Dict
import aiohttp
import asyncio
import requests
from models.abc_classes import APIFetcher, APIFetcherError
from models.weather_data import WeatherData, WeatherUnit
from models.config_classes import APIFetcherConfiguration
from models.location import Location


class OpenweatherFetcher(APIFetcher):
    def __init__(self, api_fetcher_config: APIFetcherConfiguration):
        self.config = api_fetcher_config
        self.api_key = self.config.api_key

    async def get_weather_data(self, location: Location) -> WeatherData:
        try:
            url = self._create_url(location)

            async with aiohttp.ClientSession() as session:
                task = asyncio.ensure_future(self.get_one_weather_data(session, url))
                res = await task
                weather_data = self._response_to_weather_data(res)

            return weather_data
        except aiohttp.ClientConnectorError as err:
            raise APIFetcherError(
                f"APIFetcher faced a aiohttp.ClientConnectorError: '{err}'."
            )
        except StatusNot200Error as err:
            raise APIFetcherError(
                f"APIFetcher faced a StatusNot200Error: 'Response with status_code other than 200'"
            )
        except KeyError as err:
            raise APIFetcherError(f"APIFetcher faced a KeyError: '{err}'.")
        except Exception as err:
            raise Exception(f"Unexpected exception in APIFetcher '{err}'.")

    async def get_one_weather_data(
        self, session: aiohttp.ClientSession, url: str
    ) -> WeatherData:
        async with session.get(url) as res:
            response = await res.json()
            if res.status != 200:
                raise StatusNot200Error()

            return response

    def _response_to_weather_data(self, res_json: Dict) -> WeatherData:
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

    def _create_url(self, location) -> str:
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.lat}&lon={location.lon}&units=metric&appid={self.api_key}"
        return url


class StatusNot200Error(Exception):
    pass
