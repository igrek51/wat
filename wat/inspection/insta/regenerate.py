from pathlib import Path
import sys

from wat.inspection.insta.dump import dump_snippet
from wat.inspection.insta.instaload import code


def _regenerate(src_filename: str, dst_filenames: list[str]):
    old_code: str = code.decode()
    new_code: str = dump_snippet(src_filename)
    if old_code == new_code:
        print('Insta-Load code is up to date')
        return
    replaced_contents: list[str] = []
    for dst_filename in dst_filenames:
        content = Path(dst_filename).read_text()
        assert content.count(old_code) == 1, f'cannot find current Insta-Load code in {dst_filename}'
        replaced_content = content.replace(old_code, new_code)
        assert replaced_content.count(old_code) == 0
        assert replaced_content.count(new_code) == 1
        replaced_contents.append(replaced_content)

    for i, dst_filename in enumerate(dst_filenames):
        Path(dst_filenames[i]).write_text(replaced_contents[i])
        print(f'Code replaced in {dst_filenames[i]}')


if __name__ == '__main__':
    _regenerate(sys.argv[1], sys.argv[2:])
