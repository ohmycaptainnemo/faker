from typing import Tuple, List, Literal, Set, Union
from random import randint


class Base:
    ALL: str = "*"
    ANY: str = "?"

    def create_random_integer_range_as_tuple(self, integer_range: List[int]) -> Tuple[int, int]:
        starting_integer: int = randint(*integer_range)
        ending_integer: int = randint(starting_integer, integer_range[-1])

        return starting_integer, ending_integer

    def create_list_of_unique_integers_within_a_range(self, integer_range: List[int], length: int) -> List[int]:
        set_of_integers: Set[int] = set()

        while len(set_of_integers) < length:
            set_of_integers.add(randint(*integer_range))

        return list(set_of_integers)

    def convert_tuple_range_to_increment_or_range_string(
        self, tuple_range: Tuple[Union[int, str], Union[int, str]], delimiter: Literal["-", "/"]
    ) -> str:
        return f"{tuple_range[0]}{delimiter}{tuple_range[1]}"

    def convert_list_to_delimited_string(self, integer_list: List[int]) -> str:
        return ",".join(str(item) for item in integer_list)
