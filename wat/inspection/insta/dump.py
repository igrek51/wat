import ast
import base64
from pathlib import Path
import re
import sys
import zlib
from typing import List


def dump_snippet(filename: str) -> tuple[str, str]:
    src_code: str = Path(filename).read_text()

    src_code = strip_type_hints(src_code)

    lines: List[str] = src_code.splitlines()
    lines = [line for line in lines if line.strip()]  # remove empty lines
    comment_pattern = re.compile(r'  # (.+)$')
    lines = [comment_pattern.sub('', line) for line in lines]  # trim comments
    lines = [minify_code(line) for line in lines]
    src_code = '\n'.join(lines)

    Path('.inspection_minified.py').write_text(src_code)

    bytecode: str = encode_text(src_code)
    glyph: str = encode_glyph(src_code)
    Path('wat/inspection/insta/magic_glyph.txt').write_text(glyph)
    return bytecode, glyph


def minify_code(text: str) -> str:
    if text.count(' = ') == 1:
        if not _is_in_quote(text, ' = '):
            text = text.replace(' = ', '=')
    text = text.replace('from typing import Any, Dict, List, Optional, Type, Iterable, Union', 'from typing import Any, Optional, Type')
    return text


def encode_text(text: str) -> str:
    compressed: bytes = zlib.compress(text.encode())
    b64: bytes = base64.b64encode(compressed)
    return b64.decode()


def encode_glyph(text: str) -> str:
    compressed: bytes = zlib.compress(text.encode())
    buffer: str = '🙀'  # U+1F640
    # encode each byte as 2 Unicode Combining Diacritical Marks: U+0300 - U+036F [112]
    for i in range(0, len(compressed), 1):
        b = compressed[i]
        buffer += chr(0x0300 | (b >> 4))
        buffer += chr(0x0300 | (b & 0b1111))
    return buffer


def _is_in_quote(line: str, part: str) -> bool:
    index = line.index(part)
    before = line[:index]
    after = line[index + len(part):]
    before_quotes = before.count('"') + before.count("'")
    after_quotes = after.count('"') + after.count("'")
    return before_quotes % 2 == 1 and after_quotes % 2 == 1


def strip_type_hints(code: str) -> str:
    tree = ast.parse(code, type_comments=False)
    new_tree = TypeHintStripper().visit(tree)
    new_tree = ast.fix_missing_locations(new_tree)
    return ast.unparse(new_tree)


class TypeHintStripper(ast.NodeTransformer):
    def visit_arg(self, node: ast.arg):
        if node.annotation is not None:
            node.annotation = None
        if node.type_comment is not None:
            node.type_comment = None
        return node
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        if node.returns is not None:
            node.returns = None
        if node.type_comment is not None:
            node.type_comment = None
        node.args = self.visit(node.args)
        node.body = [self.visit(child) for child in node.body]
        return node
    
    def visit_Assign(self, node: ast.Assign):
        if node.type_comment is not None:
            node.type_comment = None
        node.targets = [self.visit(target) for target in node.targets]
        return node
    
    def visit_AnnAssign(self, node: ast.AnnAssign):
        if node.value is None:
            return node
        target = self.visit(node.target)
        return ast.Assign(targets=[target], value=node.value)


if __name__ == '__main__':
    bytecode, glyph = dump_snippet(sys.argv[1])
    print(bytecode)
    print(glyph)
