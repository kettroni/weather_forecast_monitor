"""
This contains the data class definitions for configuration.
"""
from pydantic.dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Location:
    lat: float
    lon: float


@dataclass
class APIFetcherConfiguration:
    locations: List[Location]
    api_key: str


@dataclass(frozen=True)
class MonitorConfiguration:
    high_temp: float
    low_temp: float
    checking_frequency: int
