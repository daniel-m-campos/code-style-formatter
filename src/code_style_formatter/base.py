import ast
import re
from copy import copy
from typing import Set


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


def to_camel(source: str) -> str:
    camel_source = copy(source)
    for name in get_names_to_format(source):
        camel_source = re.sub(name, snake_to_camel(name), camel_source)
    return camel_source
