from pathlib import Path
import sys


# Github Markdown format into mkdocs Markdown
_replace_contents = {
    '''> [!Warning]
> Before executing **Insta-Load** snippet, it's recommended to verify what you're about to run.
> You can either:
>
> - Verify what's inside the extracted code beforehand:
>   ```python
>   print(zlib.decompress(base64.b64decode(code)).decode())
>   ```
> - Paste the content of [inspection.py](https://github.com/igrek51/wat/blob/master/wat/inspection/inspection.py) into your interpreter.
>   It has the same effect.
> - [Install package with pip](#install-with-pip) and review the code.''': '''!!! warning
    Before executing **Insta-Load** snippet, it's recommended to verify what you're about to run.
    You can either:

    - Verify what's inside the extracted code beforehand:
      ```python
      print(zlib.decompress(base64.b64decode(code)).decode())
      ```
    - Paste the content of [inspection.py](https://github.com/igrek51/wat/blob/master/wat/inspection/inspection.py) into your interpreter.
      It has the same effect.
    - [Install package with pip](#install-with-pip) and review the code.'''
}

def _generate_index():
    src_filename = 'README.md'
    dst_filename = 'docs/index.md'
    content = Path(src_filename).read_text()

    for replace_from, replace_to in _replace_contents.items():
        assert content.count(replace_from) == 1, 'cannot find replace_from pattern in source document'
        content = content.replace(replace_from, replace_to)
        assert content.count(replace_to) == 1

    content = '''---
hide:
  - navigation
---

''' + content

    Path(dst_filename).write_text(content)

    print(f'mkdocs Markdown generated for {dst_filename} from {src_filename}')


if __name__ == '__main__':
    if sys.argv[1] == 'generate-index':
        _generate_index()
    else:
        raise ValueError('Unknown command')
