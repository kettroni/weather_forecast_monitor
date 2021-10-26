from pydantic.dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ForecastData:
    lon: float
    lat: float
    high_temp: int
    low_temp: int
    exceeds_limits: bool
    timestamp: str
    forecast_id: int = 0
