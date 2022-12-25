import ast
import re
from copy import copy
from functools import reduce
from typing import Set, Callable

CAMEL_PATTERN = re.compile(r"(?<!^)(?=[A-Z])")


class FindNamesToFormat(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.names = set()

    def visit_Assign(self, node: ast.Assign):
        for target in node.targets:
            self.names.add(target.id)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.names.add(node.name)
        self.generic_visit(node)

    def visit_arguments(self, node: ast.arguments):
        for arg in node.args:
            self.names.add(arg.arg)
        self.generic_visit(node)


def get_names_to_format(source: str) -> Set[str]:
    tree = ast.parse(source)
    visitor = FindNamesToFormat()
    visitor.visit(tree)
    return visitor.names


def snake_to_camel(word: str) -> str:
    tokens = word.split("_")
    return tokens[0] + "".join(x.title() for x in tokens[1:])


def camel_to_snake(word: str) -> str:
    return word if word.isupper() else CAMEL_PATTERN.sub("_", word).lower()


def convert(source: str, converter: Callable[[str], str]) -> str:
    return reduce(
        lambda src, name: re.sub(name, converter(name), src),
        get_names_to_format(source),
        copy(source),
    )


def to_camel(snake_source: str) -> str:
    return convert(snake_source, snake_to_camel)


def to_snake(camel_module: str) -> str:
    return convert(camel_module, camel_to_snake)
