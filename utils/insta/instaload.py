import base64
import zlib
from pathlib import Path

from minify import minify_snippet, SRC_FILENAME

OUT_INSTALOAD_FILENAME = 'utils/insta/instaload.txt'


def encode_instaload(snippet: str) -> str:
    compressed: bytes = zlib.compress(snippet.encode())
    b64: bytes = base64.b64encode(compressed)
    return b64.decode()


def save_instaload() -> str:
    minified = minify_snippet(SRC_FILENAME)
    code = encode_instaload(minified)
    Path(OUT_INSTALOAD_FILENAME).write_text(code)
    return code


def decode_instaload(code: str) -> str:
    return zlib.decompress(base64.b64decode(code)).decode()


def load_instaload():
    code = Path(OUT_INSTALOAD_FILENAME).read_text()
    exec(zlib.decompress(base64.b64decode(code)).decode(), globals())


if __name__ == '__main__':
    save_instaload()
