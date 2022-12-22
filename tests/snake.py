import functools as ftools

CONST = 42

@ftools.lru_cache
def my_func(a_var: int, b_var: str = "Hello") -> None:
    print(CONST + a_var * 2, b_var)
