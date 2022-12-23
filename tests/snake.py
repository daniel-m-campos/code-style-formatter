import functools as ftools
from typing import Tuple

CONST = 42


@ftools.lru_cache
def my_func(a_var: int, b_var: str = "Hello") -> Tuple:
    return [CONST + a_var * i for i in range(2)], b_var


if __name__ == "__main__":
    result = my_func(1)
    print(*result)
