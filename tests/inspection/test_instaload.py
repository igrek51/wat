import base64
import zlib

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
