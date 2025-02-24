import zlib
from pathlib import Path

from minify import minify_snippet, SRC_FILENAME

OUT_GLYPH_FILENAME = 'utils/insta/magic_glyph.md'


def encode_glyph(snippet: str) -> str:
    compressed: bytes = zlib.compress(snippet.encode())
    return encode_glyph_bytes(compressed)


def save_glyph() -> str:
    minified = minify_snippet(SRC_FILENAME)
    glyph = encode_glyph(minified)
    Path(OUT_GLYPH_FILENAME).write_text(glyph)
    return glyph


def decode_glyph(glyph: str) -> str:
    compressed = bytes(
        ord(c) & 255
        for c in glyph[1:]
    )
    return zlib.decompress(compressed).decode()


def load_glyph():
    glyph = Path(OUT_GLYPH_FILENAME).read_text()
    exec(zlib.decompress(bytes(ord(c)&255 for c in glyph[1:])).decode(), globals())


def encode_glyph_bytes(nibbles: bytes) -> str:
    buffer: str = '🙀'  # U+1F640
    for i in range(len(nibbles)):
        b = nibbles[i]
        buffer += encode_glyph_byte(b)
    return buffer


def encode_glyph_byte(b: int) -> str:
    if b == 0xff:
        return chr(0xFEFF)  # Zero Width No-Break Space
    if b <= 0xef:
        return chr(0xe0100 | b)  # Variation Selectors Supplement: E0100-E01EF
    return chr(0x2d00 | b)  # Cyrillic Extended-A: 2DE0-2DFF


if __name__ == '__main__':
    glyph = save_glyph()
    print(glyph)
