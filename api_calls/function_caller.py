from typing import Callable
import asyncio
from context import supress


class FunctionCaller:
    def __init__(self, function: Callable, call_frequency: str):
        self.function = function
        self.call_frequency = call_frequency
