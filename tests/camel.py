import functools as ftools
from typing import Tuple

CONST = 42


@ftools.lru_cache
def myFunc(aVar: int, bVar: str = "Hello") -> Tuple:
    return [CONST + aVar * i for i in range(2)], bVar


if __name__ == "__main__":
    result = myFunc(1)
    print(*result)
