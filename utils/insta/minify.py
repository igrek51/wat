import ast
from pathlib import Path
import re
from typing import Iterable

SRC_FILENAME = 'wat/inspection/inspection.py'


def minify_snippet(filename: str) -> str:
    src_code: str = Path(filename).read_text()

    src_code = strip_type_hints(src_code)
    lines: Iterable[str] = src_code.splitlines()
    lines = (line for line in lines if line.strip())  # remove empty lines
    comment_pattern = re.compile(r'  # (.+)$')
    lines = (comment_pattern.sub('', line) for line in lines)  # trim comments
    lines = (minify_code(line) for line in lines)
    src_code = '\n'.join(lines)

    Path('utils/insta/.inspection_minified.py').write_text(src_code)
    return src_code


def minify_code(text: str) -> str:
    if text.count(' = ') == 1:
        if not _is_in_quote(text, ' = '):
            text = text.replace(' = ', '=')
    text = text.replace('from typing import Any, Dict, List, Optional, Type, Iterable, Union', 'from typing import Any, Optional, Type')
    return text


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
    minified = minify_snippet(SRC_FILENAME)
    print(minified)
