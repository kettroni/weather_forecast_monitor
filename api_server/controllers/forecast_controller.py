from flask import json
from forecast import ForecastData
from typing import List


def get_forecasts() -> List[ForecastData]:
    # TODO: fix this to get from real database
    forecasts = [
        ForecastData(
            lon=20,
            lat=20,
            high_temp=10,
            low_temp=0,
            exceeds_limits=True,
            timestamp="",
            forecast_id=0
        )
    ]
    
    return json.dumps(forecasts)


def insert_forecasts(forecasts: ForecastData) -> None:
    pass
