from pydantic.dataclasses import dataclass
from .location import Location
from .temp_limit import TempLimit


@dataclass
class MonitorData:
    location: Location
    temp_limit: TempLimit
