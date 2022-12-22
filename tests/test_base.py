import pytest


@pytest.fixture
def snake_module():
    return open("snake.py","r").read()


def test_snake_module(snake_module):
    exec(snake_module)