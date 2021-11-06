"""
This contains the data class definitions for configuration.
"""
from pydantic.dataclasses import dataclass
from typing import List
from models.monitor_target import MonitorTarget


@dataclass
class APIFetcherConfiguration:
    api_key: str


@dataclass(frozen=True)
class MonitorConfiguration:
    checking_frequency: int
    monitor_targets: List[MonitorTarget]
