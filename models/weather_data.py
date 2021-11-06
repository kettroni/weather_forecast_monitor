from typing import List
from pydantic.dataclasses import dataclass


@dataclass
class WeatherUnit:
    temp_max: float
    temp_min: float
    dt_txt: str

@dataclass
class WeatherData:
    lat: float
    lon: float
    units: List[WeatherUnit]
