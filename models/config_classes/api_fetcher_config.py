from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class APIFetcherConfiguration:
    api_key: str
