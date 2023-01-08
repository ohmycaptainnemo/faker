from enum import Enum


class ValueRangeType(Enum):
    DAY_OF_WEEK: str = "day_of_week"
    DAY_OF_MONTH: str = "day_of_month"


class DelimiterRangeType(Enum):
    INCREMENT: str = "/"
    RANGE: str = "-"
