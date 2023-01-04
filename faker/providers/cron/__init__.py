from .. import BaseProvider
from typing import Dict, Tuple, List
from random import randint


class Provider(BaseProvider):
    ALL: str = "*"
    ANY: str = "?"
    INCREMENT: str = "/"
    NTH_OCCURRENCE: str = "#"
    WEEKDAY: str = "W"
    LAST: str = "L"
    
    RANGES: Dict[str, List[int]] = {
        "minutes": [0, 59],
        "hours": [0, 23],
        "day_of_month": [1, 31],
        "month": [1, 12],
        "day_of_week": [0, 6]
    }
    
    def _create_random_integer_range(self, integer_range: List[int]):
        starting_integer: int = randint(*integer_range)
        ending_integer: int = randint(starting_integer, integer_range[-1])
        return f"{starting_integer}-{ending_integer}"
    
    