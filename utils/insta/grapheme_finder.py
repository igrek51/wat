#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "grapheme",
# ]
# ///
import grapheme

excluded = {
    0x0670, 0x0bc6, 0x0bca, 0x0cca, 0x09cb, 0x09cc, 0x036f,
    0x0a70, 0x1a70, 0x0362, 0x0962, 0x0b62, 0x0c62, 0x0d62,
    0x0e62, 0x1a62, 0x11362, 0x16f62, 0x1da62, 0x7f0, 0x7f1,
    0x8f0, 0x1bf0,
}

def _find(suffix: int) -> int | None:
    for prefix in range(0xfff):
        codepoint = (prefix << 8) | suffix
        if codepoint in excluded:
            continue
        char = chr(codepoint)
        combo = 'A' + char + char
        if grapheme.length(combo) == 1:
            return prefix
    return None


def find_0width_characters():
    """Find zero-width Unicode characters ending with the given byte"""
    for b in range(0, 256):
        prefix = _find(b)
        assert prefix is not None, 'no matching character'
        codepoint = (prefix << 8) | b
        print(f'{hex(b)}: {hex(codepoint)}')


if __name__ == '__main__':
    find_0width_characters()
