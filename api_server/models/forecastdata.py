from pydantic.dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ForecastData:
    lon: float
    lat: float
    low_temp: float
    high_temp: float
    exceeds_limits: bool
    timestamp: str
    forecast_id: int = 0
