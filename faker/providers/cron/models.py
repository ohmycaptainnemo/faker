from typing import List, Dict, Union, Callable
from random import randint, choice

from .base import Base


class Minute(Base):
    def __init__(self):
        super(Minute, self).__init__()
        self.minute_range: List[int] = [0, 59]
        self.random_choices: Union[Callable, str] = [
            self.ALL,
            self.ANY,
            str(randint(*self.minute_range)),
            lambda: self.convert_tuple_range_to_increment_or_range_string(
                self.create_random_integer_range_as_tuple(self.minute_range), choice(["-", "/"])
            ),
            lambda: self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*self.minute_range)), "/"),
            lambda: self.convert_list_to_delimited_string(
                self.create_list_of_unique_integers_within_a_range(self.minute_range, randint(2, randint(3, 10)))
            ),
        ]

    def create_random_minute(self) -> str:
        return self.select_random_option_from_list(self.random_choices)


class Hour(Base):
    def __init__(self):
        super(Hour, self).__init__()
        self.hour_range: List[int] = [0, 23]
        self.random_choices: Union[Callable, str] = [
            self.ALL,
            self.ANY,
            str(randint(self.hour_range)),
            lambda: self.convert_tuple_range_to_increment_or_range_string(
                self.create_random_integer_range_as_tuple(self.hour_range), choice(["-", "/"])
            ),
            lambda: self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*self.hour_range)), "/"),
            lambda: self.convert_list_to_delimited_string(
                self.create_list_of_unique_integers_within_a_range(self.hour_range, randint(2, randint(3, 10)))
            ),
        ]

    def create_random_hour(self) -> str:
        return self.select_random_option_from_list(self.random_choices)


class DayOfMonth(Base):
    def __init__(self):
        super(DayOfMonth, self).__init__()
        self.day_of_month_range: List[int] = [1, 31]
        self.random_choices: Union[Callable, str] = [
            self.ALL,
            self.ANY,
            str(randint(self.day_of_month_range)),
            lambda: self.convert_tuple_range_to_increment_or_range_string(
                self.create_random_integer_range_as_tuple(self.day_of_month_range), choice(["-", "/"])
            ),
            lambda: self.convert_tuple_range_to_increment_or_range_string(
                (self.ALL, randint(*self.day_of_month_range)), "/"
            ),
            lambda: self.convert_list_to_delimited_string(
                self.create_list_of_unique_integers_within_a_range(self.day_of_month_range, randint(2, randint(3, 10)))
            ),
            lambda: self.create_day_of_month_expression(),
            lambda: self.create_nth_last_day_of_month_string(),
        ]

    def create_random_day_of_month(self) -> str:
        return self.select_random_option_from_list(self.random_choices)


class Month(Base):
    def __init__(self):
        super(Month, self).__init__()
        self.month_range: List[int] = [1, 12]

        self.months_alpha_numeric_mapping: Dict[int, str] = {
            1: "jan",
            2: "feb",
            3: "mar",
            4: "apr",
            5: "may",
            6: "jun",
            7: "jul",
            8: "aug",
            9: "sep",
            10: "oct",
            11: "nov",
            12: "dec",
        }
        self.random_choices: Union[Callable, str] = [
            self.ALL,
            self.ANY,
            str(randint(self.month_range)),
            lambda: self.convert_tuple_range_to_increment_or_range_string(
                self.create_random_integer_range_as_tuple(self.month_range), choice(["-", "/"])
            ),
            lambda: self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*self.month_range)), "/"),
            lambda: self.convert_list_to_delimited_string(
                self.create_list_of_unique_integers_within_a_range(self.month_range, randint(2, randint(3, 10)))
            ),
            lambda: self.convert_integer_list_to_delimited_string_mapping(
                self.create_list_of_unique_integers_within_a_range(self.month_range, randint(2, randint(3, 10))),
                self.months_alpha_numeric_mapping
                choice([True, False]),
            ),
        ]

    def create_random_month(self) -> str:
        return self.select_random_option_from_list(self.random_choices)


class DayOfWeek(Base):
    def __init__(self):
        super(DayOfWeek, self).__init__()
        self.week_range: List[int] = [0, 6]

        self.weeks_alpha_numeric_mapping: Dict[int, str] = {
            0: "sun",
            1: "mon",
            2: "tue",
            3: "wed",
            4: "thu",
            5: "fri",
            6: "sat",
        }
        self.random_choices: Union[Callable, str] = [
            self.ALL,
            self.ANY,
            str(randint(self.week_range)),
            lambda: self.convert_tuple_range_to_increment_or_range_string(
                self.create_random_integer_range_as_tuple(self.week_range), choice(["-", "/"])
            ),
            lambda: self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*self.week_range)), "/"),
            lambda: self.convert_list_to_delimited_string(
                self.create_list_of_unique_integers_within_a_range(self.week_range, randint(2, randint(3, 10)))
            ),
            lambda: self.convert_integer_list_to_delimited_string_mapping(
                self.create_list_of_unique_integers_within_a_range(self.week_range, randint(2, randint(3, 10))),
                self.weeks_alpha_numeric_mapping,
                choice([True, False]),
            ),
        ]

    def create_random_day_of_week(self) -> str:
        return self.select_random_option_from_list(self.random_choices)
