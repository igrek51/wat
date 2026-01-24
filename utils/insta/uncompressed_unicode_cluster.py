from pathlib import Path

from minify import minify_snippet, SRC_FILENAME

OUT_RAW_CLUSTER_FILENAME = 'utils/insta/uncompressed_unicode_cluster.md'


def save_raw_cluster() -> str:
    minified: str = minify_snippet(SRC_FILENAME)
    minified = minified.replace('    ', '\t')
    glyph: str = encode_glyph_bytes(minified.encode())
    Path(OUT_RAW_CLUSTER_FILENAME).write_text(glyph)
    return glyph


def encode_glyph_bytes(nibbles: bytes) -> str:
    buffer: str = ''
    for i in range(len(nibbles)):
        b: int = nibbles[i]
        if i == 0:  # first code point has to be real
            buffer += chr(b)
        else:
            buffer += encode_glyph_byte(b)
    return buffer


def encode_glyph_byte(b: int) -> str:
    if b == 0xff:
        return chr(0xFEFF)  # Zero Width No-Break Space
    if b <= 0xef:
        return chr(0xe0100 | b)  # Variation Selectors Supplement: E0100-E01EF
    return chr(0x2d00 | b)  # Cyrillic Extended-A: 2DE0-2DFF


def load_glyph():
    g = Path(OUT_RAW_CLUSTER_FILENAME).read_text()
    # print(bytes(ord(c)&255 for c in g).decode())
    exec(bytes(ord(c)&255 for c in g), globals())


if __name__ == '__main__':
    glyph = save_raw_cluster()
    print(f'Packed into {len(glyph)} bytes')
    print(glyph)
    load_glyph()
