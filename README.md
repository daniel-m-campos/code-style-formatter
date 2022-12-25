# Code Style Formatter
A small tool for converting between snake and camel case naming conventions.

## Example
### Snake to Camel Case
```python
# Snake case source
source = """import functools as ftools
from typing import Tuple

CONST = 42


@ftools.lru_cache
def my_func(a_var: int, b_var: str = "Hello") -> Tuple:
    return [CONST + a_var * i for i in range(2)], b_var


if __name__ == "__main__":
    result = my_func(1)
    print(*result)
"""

# Convert using code_style_converter

import code_style_formatter as csf

dest = csf.to_camel(source)

# Print newly converted camel case source

print(dest)
"""import functools as ftools
from typing import Tuple

CONST = 42


@ftools.lru_cache
def myFunc(aVar: int, bVar: str = "Hello") -> Tuple:
    return [CONST + aVar * i for i in range(2)], bVar


if __name__ == "__main__":
    result = myFunc(1)
    print(*result)
"""
```