from pydantic.dataclasses import dataclass
from models.location import Location
from models.templimit import TempLimit


@dataclass
class MonitorTarget:
    location: Location
    temp_limit: TempLimit
