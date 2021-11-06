from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class TempLimit:
    low_temp: float
    high_temp: float

    def __str__(self):
        if self.high_temp < 0:
            return f"{self.low_temp}-({self.high_temp})"
        else:
            return f"{self.low_temp}-{self.high_temp}"
