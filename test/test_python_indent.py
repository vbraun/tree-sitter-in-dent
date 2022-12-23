from tree_sitter import Parser
from dent.languages import PY_LANGUAGE

parser = Parser()
parser.set_language(PY_LANGUAGE)

src = bytes("""
def foo():
    if bar:
        baz()
""", "utf8")

def read_callable(byte_offset, point):
    return src[byte_offset:byte_offset+1]

tree = parser.parse(read_callable)
