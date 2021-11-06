from typing import List
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class WeatherUnit:
    temp_max: float
    temp_min: float
    dt_txt: str


@dataclass(frozen=True)
class WeatherData:
    lat: float
    lon: float
    units: List[WeatherUnit]
