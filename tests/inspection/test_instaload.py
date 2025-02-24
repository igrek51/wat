import base64
import zlib
from pathlib import Path

from wat.inspection.insta.instaload import code
from tests.asserts import assert_multiline_match, StdoutCap


def test_load_instaload_snippet():
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
    glyph = Path('wat/inspection/insta/magic_glyph.txt').read_text()
    exec(zlib.decompress(bytes(ord(glyph[i])<<4&240|ord(glyph[i+1])&15 for i in range(1,len(glyph),2))).decode(), globals())
    assert wat.short.str / 'WAT is going on?' == '''value: 'WAT is going on?'
type: str
len: 16'''
