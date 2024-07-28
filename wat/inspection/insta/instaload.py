import base64, zlib
code = b'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'
exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
