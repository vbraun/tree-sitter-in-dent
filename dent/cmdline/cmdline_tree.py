import logging
from typing import Sequence

from tree_sitter import Parser

from dent.lang_ts.language import LANGUAGE
from dent.util.pretty_print import pretty_print


def dent_cmdline_tree(filename: str) -> None:
    with open(filename, 'rb') as f:
        src = f.read()
    parser = Parser()
    parser.set_language(LANGUAGE)
    tree = parser.parse(src)
    pretty_print(tree)
    


