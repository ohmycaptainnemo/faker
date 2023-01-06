from .. import BaseProvider
from typing import Dict, Tuple, List, Literal, Set
from random import randint, choice


class Provider(BaseProvider):
    ALL: str = "*"
    ANY: str = "?"

    RANGES: Dict[str, List[int]] = {
        "minutes": [0, 59],
        "hours": [0, 23],
        "day_of_month": [1, 31],
        "month": [1, 12],
        "day_of_week": [0, 6],
    }

    MONTHS_ALPHA_NUMERIC_MAPPING: Dict[int, str] = {
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

    WEEK_DAYS_ALPHA_NUMERIC_MAPPING: Dict[int, str] = {
        0: "sun",
        1: "mon",
        2: "tue",
        3: "wed",
        4: "thu",
        5: "fri",
        6: "sat",
    }

    def _create_random_integer_range_as_tuple(self, integer_range: List[int]) -> Tuple[int, int]:
        starting_integer: int = randint(*integer_range)
        ending_integer: int = randint(starting_integer, integer_range[-1])

        return starting_integer, ending_integer

    def _create_list_of_unique_integers_within_a_range(self, integer_range: List[int], length: int) -> List[int]:
        set_of_integers: Set[int] = set()

        while len(set_of_integers) < length:
            set_of_integers.add(randint(*integer_range))

        return list(set_of_integers)

    def _create_nth_last_day_of_month_string(self) -> str:
        return f"""L-{randint(*Provider.RANGES["day_of_month"])}"""

    def _create_nth_last_day_of_week_string(self) -> str:
        return f"""{randint(*Provider.RANGES["day_of_week"])}L"""

    def _create_day_of_month_expression(self):
        return f"""{randint(*Provider.RANGES["day_of_month"])}W"""

    def _create_nth_weekday_expression(self):
        return f"""{randint(*Provider.RANGES["day_of_week"])}#{randint(1,5)}"""

    def _convert_tuple_range_to_increment_or_range_string(
        self, tuple_range: Tuple[int, int], delimiter: Literal["-", "/"]
    ) -> str:
        return f"{tuple_range[0]}{delimiter}{tuple_range[1]}"

    def _convert_list_to_delimited_string(self, integer_list: List[int]) -> str:
        return ",".join(str(item) for item in integer_list)

    def _convert_week_or_month_integer_list_to_delimited_string_mapping(
        self,
        integer_list: List[int],
        index_interpretation: Literal["weekday", "month"],
        make_result_uniform: bool = True,
    ) -> str:
        string_mapping_list: List[str] = []

        for item in integer_list:
            if make_result_uniform:
                string_mapping: str = self._convert_week_or_month_integer_to_string_mapping(item, index_interpretation)
            else:
                string_mapping: str = str(item)
            string_mapping_list.append(string_mapping)

        return self._convert_integer_list_to_delimited_string(string_mapping_list)

    def _convert_week_or_month_integer_to_string_mapping(
        self, key: int, index_interpretation: Literal["weekday", "month"]
    ) -> str:
        if index_interpretation == "month":
            return Provider.MONTHS_ALPHA_NUMERIC_MAPPING[key]
        else:
            return Provider.WEEK_DAYS_ALPHA_NUMERIC_MAPPING[key]

    def _convert_tuple_range_to_week_month_string_mapping(
        self,
        integer_tuple: Tuple[int, int],
        index_interpretation: Literal["weekday", "month"],
        delimiter: Literal["-", "/"],
        is_start_string_mapping: bool = True,
        is_end_string_mapping: bool = True,
    ) -> str:
        if is_start_string_mapping:
            start: str = self._convert_week_or_month_integer_to_string_mapping(integer_tuple[0], index_interpretation)
        else:
            start: str = str(integer_tuple[0])
        if is_end_string_mapping:
            end: str = self._convert_week_or_month_integer_to_string_mapping(integer_tuple[1], index_interpretation)
        else:
            end: str = str(integer_tuple[1])

        return f"{start}{delimiter}{end}"

    def _create_random_minutes(self):
        choice(
            [
                str(randint(*Provider.RANGES["minutes"])),
                self._convert_tuple_range_to_string(
                    self._create_random_integer_range_as_tuple(Provider.RANGES["minutes"])
                ),
            ]
        )
