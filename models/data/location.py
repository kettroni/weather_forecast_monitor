from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    lat: float
    lon: float
