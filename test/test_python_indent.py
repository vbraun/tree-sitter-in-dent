from tree_sitter import Parser

from dent.lang_py.language import LANGUAGE

parser = Parser()
parser.set_language(LANGUAGE)

src = bytes("""
def foo():
    if bar:
        baz()
""", "utf8")


def read_callable(byte_offset: int, point: bytes) -> bytes:
    return src[byte_offset:byte_offset + 1]


tree = parser.parse(read_callable)  # type: ignore
