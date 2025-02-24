import base64
import zlib
from pathlib import Path

from tests.asserts import assert_multiline_match, StdoutCap


def test_load_instaload_snippet():
    code = Path('utils/insta/instaload.txt').read_text()
    snippet = zlib.decompress(base64.b64decode(code)).decode()
    assert 'wat=Wat()' in snippet.splitlines()
    
    exec(snippet, globals())
    with StdoutCap() as capture:
        wat.short / 'moo'
    assert_multiline_match(capture.output(), r'''
value: 'moo'
type: str
len: 3
''')


def test_load_from_magic_glyph():
    glyph = Path('utils/insta/magic_glyph.md').read_text()
    exec(zlib.decompress(bytes(ord(c)&255 for c in glyph[1:])).decode(), globals())
    assert wat.short.str / 'WAT is going on?' == '''value: 'WAT is going on?'
type: str
len: 16'''
