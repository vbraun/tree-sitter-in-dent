import unittest
from functools import cached_property

from tree_sitter import Parser

from dent.lang_py.language import LANGUAGE

src = """
def foo():
    if bar:
        baz()
"""


class TestLangPythonInstalled(unittest.TestCase):

    @cached_property
    def parser(self) -> Parser:
        parser = Parser()
        parser.set_language(LANGUAGE)
        return parser

    def test_python_installed(self) -> None:
        tree = self.parser.parse(src.encode('utf-8'))
        self.assertEqual(
            tree.root_node.sexp(),
            "(module "
                "(function_definition "   # noqa
                    "name: (identifier) "   # noqa
                    "parameters: (parameters) "   # noqa
                    "body: (block "   # noqa
                        "(if_statement "   # noqa
                            "condition: (identifier) "   # noqa
                            "consequence: (block "   # noqa
                                "(expression_statement "   # noqa
                                    "(call "   # noqa
                                        "function: (identifier) "   # noqa
                                        "arguments: (argument_list))))))))"   # noqa
        )
