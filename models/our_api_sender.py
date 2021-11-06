from typing import Dict
import asyncio
import aiohttp
from dataclasses import asdict
from models.abc_classes import APISender, APISenderError
from models.forecast_data import ForecastData


class OurApiSender(APISender):
    def __init__(self, url: str):
        self.url = url

    async def send_forecast_data(self, data: ForecastData):
        try:
            async with aiohttp.ClientSession() as session:
                forecast_as_dict = asdict(data)

                data_json = {"forecasts": [forecast_as_dict]}

                task = asyncio.ensure_future(
                    self.post_one_forecast_data(session, self.url, data_json)
                )
                status_code = await task

                return status_code
        except aiohttp.ClientConnectorError as err:
            raise APISenderError(
                f"APISender faced a aiohttp.ClientConnectorError: '{err}'."
            )
        except Exception as err:
            raise Exception(f"Unexpected exception in APIFetcher '{err}'.")

    async def post_one_forecast_data(
        self, session: aiohttp.ClientSession, url: str, data_as_json: Dict
    ) -> int:
        async with session.post(url, json=data_as_json) as res:
            status_code = res.status

            return status_code
