import ast
import re
from copy import copy
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


def format(source: str, converter: Callable[[str], str]) -> str:
    dest = copy(source)
    for name in get_names_to_format(source):
        dest = re.sub(name, converter(name), dest)
    return dest


def to_camel(snake_source: str) -> str:
    return format(snake_source, snake_to_camel)


def to_snake(camel_module: str) -> str:
    return format(camel_module, camel_to_snake)
