import base64
import zlib


def load_snippet(code: str):
    text: str = decode_text(code)
    exec(text, globals())


def decode_text(code: str) -> str:
    b64: bytes = code.encode()
    compressed = base64.b64decode(b64)
    decompressed: bytes = zlib.decompress(compressed)
    return decompressed.decode()
