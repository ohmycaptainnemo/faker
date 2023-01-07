from typing import List, Dict, Literal, Tuple
from random import randint, choice

from .base import Base


class Minute(Base):
    minute_range: List[int] = [0, 59]

    def create_random_minute(self, list_length: int) -> str:
        return choice(
            [
                self.ALL,
                self.ANY,
                str(randint(*Minute.minute_range)),
                self.convert_tuple_range_to_increment_or_range_string(
                    self.create_random_integer_range_as_tuple(Minute.minute_range), choice(["-", "/"])
                ),
                self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*Minute.minute_range)), "/"),
                # TODO: For everything below add a case where a comma separated list can be generated that also
                # includes cases such as */5,4,7-9 * * * *.
                self.convert_list_to_delimited_string(
                    self.create_list_of_unique_integers_within_a_range(Minute.minute_range, randint(2, list_length))
                ),
            ]
        )


class Hour(Base):
    hour_range: List[int] = [0, 23]

    def create_random_hour(self, list_length: int) -> str:
        return choice(
            [
                self.ALL,
                self.ANY,
                str(randint(*Hour.hour_range)),
                self.convert_tuple_range_to_increment_or_range_string(
                    self.create_random_integer_range_as_tuple(Hour.hour_range), choice(["-", "/"])
                ),
                self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*Hour.hour_range)), "/"),
                self.convert_list_to_delimited_string(
                    self.create_list_of_unique_integers_within_a_range(Hour.hour_range, randint(2, list_length))
                ),
            ]
        )


class DayOfMonth(Base):
    day_of_month_range: List[int] = [1, 31]

    def create_day_of_month_expression(self):
        return f"""{randint(*DayOfMonth.day_of_month_range)}W"""

    def create_nth_last_day_of_month_string(self) -> str:
        return f"""L-{randint(*DayOfMonth.day_of_month_range)}"""

    def create_random_day_of_month(self, list_length: int) -> str:
        return choice(
            [
                self.ALL,
                self.ANY,
                str(randint(*DayOfMonth.day_of_month_range)),
                self.convert_tuple_range_to_increment_or_range_string(
                    self.create_random_integer_range_as_tuple(DayOfMonth.day_of_month_range), choice(["-", "/"])
                ),
                self.convert_tuple_range_to_increment_or_range_string(
                    (self.ALL, randint(*DayOfMonth.day_of_month_range)), "/"
                ),
                self.convert_list_to_delimited_string(
                    self.create_list_of_unique_integers_within_a_range(
                        DayOfMonth.day_of_month_range, randint(2, list_length)
                    )
                ),
                self.create_day_of_month_expression(),
                self.create_nth_last_day_of_month_string(),
            ]
        )


class Month(Base):
    month_range: List[int] = [1, 12]

    months_alpha_numeric_mapping: Dict[int, str] = {
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

    def convert_month_integer_to_string_mapping(self, key: int) -> str:
        return Month.months_alpha_numeric_mapping[key]

    def convert_month_integer_list_to_delimited_string_mapping(
        self,
        integer_list: List[int],
        make_result_uniform: bool = True,
    ) -> str:
        string_mapping_list: List[str] = []

        for item in integer_list:
            if make_result_uniform:
                string_mapping: str = self.convert_month_integer_to_string_mapping(item)
            else:
                string_mapping: str = choice([str(item), self.convert_month_integer_to_string_mapping(item)])
            string_mapping_list.append(string_mapping)

        return self.convert_list_to_delimited_string(string_mapping_list)

    def convert_tuple_range_to_month_string_mapping(
        self,
        integer_tuple: Tuple[int, int],
        delimiter: Literal["-", "/"],
        is_start_string_mapping: bool = True,
        is_end_string_mapping: bool = True,
    ) -> str:
        if is_start_string_mapping:
            start: str = self.convert_month_integer_to_string_mapping(integer_tuple[0])
        else:
            start: str = str(integer_tuple[0])
        if is_end_string_mapping:
            end: str = self.convert_month_integer_to_string_mapping(integer_tuple[1])
        else:
            end: str = str(integer_tuple[1])

        return f"{start}{delimiter}{end}"

    def create_random_month(self, list_length: int) -> str:
        return choice(
            [
                self.ALL,
                self.ANY,
                str(randint(*Month.month_range)),
                self.convert_tuple_range_to_increment_or_range_string(
                    self.create_random_integer_range_as_tuple(Month.month_range), choice(["-", "/"])
                ),
                self.convert_tuple_range_to_increment_or_range_string((self.ALL, randint(*Month.month_range)), "/"),
                self.convert_list_to_delimited_string(
                    self.create_list_of_unique_integers_within_a_range(Month.month_range, randint(2, list_length))
                ),
                self.convert_list_to_delimited_string(
                    self.convert_month_integer_list_to_delimited_string_mapping(
                        self.create_list_of_unique_integers_within_a_range(Month.month_range, randint(2, list_length)),
                        choice([True, False]),
                    )
                ),
            ]
        )


class DayOfWeek(Base):
    week_range: List[int] = [0, 6]

    weeks_alpha_numeric_mapping: Dict[int, str] = {
        0: "sun",
        1: "mon",
        2: "tue",
        3: "wed",
        4: "thu",
        5: "fri",
        6: "sat",
    }

    def create_nth_last_day_of_week_string(self) -> str:
        return f"""{randint(*DayOfWeek.week_range)}L"""

    def create_nth_weekday_expression(self):
        return f"""{randint(*DayOfWeek.week_range)}#{randint(1,5)}"""

    def convert_week_integer_to_string_mapping(self, key: int) -> str:
        return DayOfWeek.weeks_alpha_numeric_mapping[key]

    def convert_week_integer_list_to_delimited_string_mapping(
        self,
        integer_list: List[int],
        make_result_uniform: bool = True,
    ) -> str:
        string_mapping_list: List[str] = []

        for item in integer_list:
            if make_result_uniform:
                string_mapping: str = self.convert_week_integer_to_string_mapping(item)
            else:
                string_mapping: str = choice([str(item), self.convert_week_integer_to_string_mapping(item)])
            string_mapping_list.append(string_mapping)

        return self.convert_list_to_delimited_string(string_mapping_list)

    def convert_tuple_range_to_week_string_mapping(
        self,
        integer_tuple: Tuple[int, int],
        delimiter: Literal["-", "/"],
        is_start_string_mapping: bool = True,
        is_end_string_mapping: bool = True,
    ) -> str:
        if is_start_string_mapping:
            start: str = self.convert_week_integer_to_string_mapping(integer_tuple[0])
        else:
            start: str = str(integer_tuple[0])
        if is_end_string_mapping:
            end: str = self.convert_week_integer_to_string_mapping(integer_tuple[1])
        else:
            end: str = str(integer_tuple[1])

        return f"{start}{delimiter}{end}"
