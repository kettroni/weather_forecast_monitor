"""
This contains the data class definitions for configuration.
"""
from pydantic.dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Location:
    lat: float
    lon: float


@dataclass(frozen=True)
class MonitorConfiguration:
    locations: List[Location]
    high_temp: float
    low_temp: float
    checking_frequency: int
