"""
This contains the data class definitions for configuration.
"""
from pydantic.dataclasses import dataclass
from typing import List
from models.location import Location


@dataclass
class APIFetcherConfiguration:
    api_key: str


@dataclass(frozen=True)
class MonitorConfiguration:
    high_temp: float
    low_temp: float
    checking_frequency: int
    locations: List[Location]
