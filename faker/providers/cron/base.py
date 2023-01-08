from typing import Tuple, List, Callable, Set, Union, Dict
from inspect import isfunction
from random import randint, choice

from enums import ValueRangeType, DelimiterRangeType


class Base:
    def __init__(self):
        self.ALL: str = "*"
        self.ANY: str = "?"

    def create_random_integer_range_as_tuple(self, integer_range: List[int]) -> Tuple[int, int]:
        starting_integer: int = randint(*integer_range)
        if starting_integer == 0:
            starting_integer += 1
        ending_integer: int = randint(starting_integer, integer_range[-1])

        return starting_integer, ending_integer

    def create_list_of_unique_integers_within_a_range(self, integer_range: List[int], length: int) -> List[int]:
        set_of_integers: Set[int] = set()

        while len(set_of_integers) < length:
            set_of_integers.add(randint(*integer_range))

        return list(set_of_integers)

    def create_day_of_month_expression(self, day_of_month_range: List[int]):
        return f"""{randint(*day_of_month_range)}W"""

    def create_nth_last_day_of_month_string(self, value_range: List[int], value_range_type: ValueRangeType) -> str:
        if value_range_type.value == "day_of_month":
            return f"""L-{randint(*value_range)}"""
        else:
            return f"""{randint(*value_range)}L"""

    def create_nth_weekday_expression(self, value_range: List[int]):
        return f"""{randint(*value_range)}#{randint(1,5)}"""

    def select_random_option_from_list(self, option_list: List[Union[Callable, str]]) -> str:
        random_choice: Union[Callable, str] = choice(option_list)

        if isfunction(random_choice):
            return random_choice()
        return random_choice

    def convert_integer_to_string_mapping(self, key: int, mapping: Dict[int, str]) -> str:
        return mapping[key]

    def convert_integer_list_to_delimited_string_mapping(
        self,
        integer_list: List[int],
        mapping: Dict[int, str],
        make_result_uniform: bool = True,
    ) -> str:
        string_mapping_list: List[str] = []

        for item in integer_list:
            if make_result_uniform:
                string_mapping: str = self.convert_integer_to_string_mapping(item, mapping)
            else:
                string_mapping: str = choice([str(item), self.convert_integer_to_string_mapping(item, mapping)])
            string_mapping_list.append(string_mapping)

        return self.convert_list_to_delimited_string(string_mapping_list)

    def convert_tuple_range_to_string_mapping(
        self,
        integer_tuple: Tuple[int, int],
        mapping: Dict[int, str],
        delimiter: DelimiterRangeType,
        is_start_string_mapping: bool = True,
        is_end_string_mapping: bool = True,
    ) -> str:
        if is_start_string_mapping:
            start: str = self.convert_integer_to_string_mapping(integer_tuple[0], mapping)
        else:
            start: str = str(integer_tuple[0])
        if is_end_string_mapping:
            end: str = self.convert_integer_to_string_mapping(integer_tuple[1], mapping)
        else:
            end: str = str(integer_tuple[1])

        return f"{start}{delimiter.value}{end}"

    def convert_tuple_range_to_increment_or_range_string(
        self, tuple_range: Tuple[Union[int, str], Union[int, str]], delimiter: DelimiterRangeType
    ) -> str:
        return f"{tuple_range[0]}{delimiter.value}{tuple_range[1]}"

    def convert_list_to_delimited_string(self, item_list: List[Union[int, str]]) -> str:
        delimited_string: str = ",".join(str(item) for item in item_list)
        return delimited_string
