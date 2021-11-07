from pydantic.dataclasses import dataclass
from typing import List
from models.data import MonitorData


@dataclass(frozen=True)
class MonitorConfiguration:
    checking_frequency: int
    monitor_datas: List[MonitorData]
