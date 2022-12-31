import unittest
from functools import cached_property

from tree_sitter import Parser

from dent.lang_py.language import LANGUAGE
from dent.util.pretty_print import pretty_format, pretty_print

src = """
def foo():
    if bar:
        baz(1)
    frob(2)
gulp(3, y=4)
"""


pretty = r"""
module [(1, 0):(6, 0)]  code='def f...=4)\n'
    function_definition [(1, 0):(4, 11)]  code='def f...ob(2)'
        def [(1, 0):(1, 3)]  code='def'
        identifier [(1, 4):(1, 7)]  code='foo'
        parameters [(1, 7):(1, 9)]  code='()'
            ( [(1, 7):(1, 8)]  code='('
            ) [(1, 8):(1, 9)]  code=')'
        block [(2, 4):(4, 11)]  code='if ba...ob(2)'
            if_statement [(2, 4):(3, 14)]  code='if ba...az(1)'
                if [(2, 4):(2, 6)]  code='if'
                identifier [(2, 7):(2, 10)]  code='bar'
                : [(2, 10):(2, 11)]  code=':'
                block [(3, 8):(3, 14)]  code='baz(1)'
                    expression_statement [(3, 8):(3, 14)]  code='baz(1)'
                        call [(3, 8):(3, 14)]  code='baz(1)'
                            identifier [(3, 8):(3, 11)]  code='baz'
                            argument_list [(3, 11):(3, 14)]  code='(1)'
                                ( [(3, 11):(3, 12)]  code='('
                                integer [(3, 12):(3, 13)]  code='1'
                                ) [(3, 13):(3, 14)]  code=')'
                call [(4, 4):(4, 11)]  code='frob(2)'
                    identifier [(4, 4):(4, 8)]  code='frob'
                    argument_list [(4, 8):(4, 11)]  code='(2)'
                        ( [(4, 8):(4, 9)]  code='('
                        integer [(4, 9):(4, 10)]  code='2'
                        ) [(4, 10):(4, 11)]  code=')'
        call [(5, 0):(5, 12)]  code='gulp(3, y=4)'
            identifier [(5, 0):(5, 4)]  code='gulp'
            argument_list [(5, 4):(5, 12)]  code='(3, y=4)'
                ( [(5, 4):(5, 5)]  code='('
                integer [(5, 5):(5, 6)]  code='3'
                , [(5, 6):(5, 7)]  code=','
                keyword_argument [(5, 8):(5, 11)]  code='y=4'
                    identifier [(5, 8):(5, 9)]  code='y'
                    = [(5, 9):(5, 10)]  code='='
                    integer [(5, 10):(5, 11)]  code='4'
"""


class TestPrettyPrint(unittest.TestCase):

    maxDiff = None
    
    @cached_property
    def parser(self) -> Parser:
        parser = Parser()
        parser.set_language(LANGUAGE)
        return parser

    def test_pretty_format(self) -> None:
        tree = self.parser.parse(src.encode('utf-8'))
        self.assertEqual(pretty_format(tree).strip(), pretty.strip())
