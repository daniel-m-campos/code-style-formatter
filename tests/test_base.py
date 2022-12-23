import pytest

from code_style_formatter import base


@pytest.fixture
def snake_module():
    return open("snake.py", "r").read()


@pytest.fixture
def camel_module():
    return open("camel.py", "r").read()


def test_snake_module(snake_module):
    exec(snake_module)


def test_camel_module(camel_module):
    exec(camel_module)


def test_get_names_to_format(snake_module):
    actual = base.get_names_to_format(snake_module)
    assert actual == {
        "CONST",
        "a_var",
        "b_var",
        "my_func",
        "result",
    }


def test_snake_to_camel(snake_module, camel_module):
    actual = base.to_camel(snake_module)
    assert actual == camel_module
