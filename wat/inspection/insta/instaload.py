import base64
import zlib

code = b'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'

if __name__ == '__main__':
    exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
