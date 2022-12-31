from typing import Iterable, Optional

from tree_sitter import Tree
from tree_sitter.binding import Node, TreeCursor


def _ellipsize_code(text: Optional[str]) -> str:
    if text is None:
        return '<missing>'
    max_len = 15
    text = repr(text)
    if len(text) < max_len:
        return text
    n = (min(max_len, len(text)) - 3) // 2
    return text[:n] + '...' + text[len(text) - n:]


def _format_node(cursor: TreeCursor, indent: int) -> Iterable[str]:
    node: Node = cursor.node
    space = ' ' * indent
    code = _ellipsize_code(node.text.decode('utf-8'))
    field_name = cursor.current_field_name()
    field_prefix = (field_name + ': ') if field_name else ''
    yield f'{space}{field_prefix}{node.type} [{node.start_point}:{node.end_point}]  code={code}'


def _line_iter(cursor: TreeCursor, indent: int) -> Iterable[str]:
    depth = 0
    yield from _format_node(cursor, depth * indent)
    while True:
        if cursor.goto_first_child():
            depth += 1
            # yield f'child {depth}'
            yield from _format_node(cursor, depth * indent)
            continue
        if cursor.goto_next_sibling():
            # yield f'sibling {depth}'
            yield from _format_node(cursor, depth * indent)
            continue
        while True:   # go to the first sibling of any parent
            if not cursor.goto_parent():
                assert depth == 0
                return
            depth -= 1
            # yield f'parent {depth}'
            if cursor.goto_next_sibling():
                # yield f'parent sibling {depth}'
                yield from _format_node(cursor, depth * indent)
                break


def pretty_format(tree: Tree, indent: int = 4) -> str:
    cursor = tree.walk()
    print(dir(cursor.node))
    return '\n'.join(_line_iter(cursor, indent))


def pretty_print(tree: Tree, indent: int = 4) -> None:
    print(pretty_format(tree, indent))
