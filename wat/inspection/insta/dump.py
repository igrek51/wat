import base64
from pathlib import Path
import re
import sys
import zlib
from typing import List


def dump_snippet(filename: str) -> str:
    text: str = Path(filename).read_text()
    lines: List[str] = text.splitlines()
    lines = [line for line in lines if line.strip()]  # remove empty lines
    comment_pattern = re.compile(r'  # (.+)$')
    lines = [comment_pattern.sub('', line) for line in lines]  # trim comments
    # trim type hints
    # remove spaces: , = : == + *
    text = '\n'.join(lines)
    code: str = encode_text(text)
    return code


def encode_text(text: str) -> str:
    compressed = zlib.compress(text.encode())
    b64: bytes = base64.b64encode(compressed)
    return b64.decode()


if __name__ == '__main__':
    print(dump_snippet(sys.argv[1]))
