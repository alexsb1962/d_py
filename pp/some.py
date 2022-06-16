from dataclasses import dataclass
import math


@dataclass
class SomeData:
    v1: int = 5
    v2: float = math.pi


s = SomeData()

dir(s)

