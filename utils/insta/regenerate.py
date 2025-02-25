from pathlib import Path

from instaload import OUT_INSTALOAD_FILENAME, save_instaload
from magic_glyph import OUT_GLYPH_FILENAME, save_glyph


def _regenerate(src_filename: str, dst_filenames: list[str]):
    old_instaload: str = Path(OUT_INSTALOAD_FILENAME).read_text()
    old_glyph: str = Path(OUT_GLYPH_FILENAME).read_text()
    new_instaload = save_instaload()
    new_glyph = save_glyph()
    replaced_contents: list[str] = []
    print(f'Insta-Load code ({len(new_instaload)} characters):\n{new_instaload}\n')
    print(f'Magic Glyph: {new_glyph}')
    
    for dst_filename in dst_filenames:
        content = Path(dst_filename).read_text()

        assert content.count(old_instaload) == 1, f'cannot find current Insta-Load code in {dst_filename}'
        replaced_content = content.replace(old_instaload, new_instaload)
        assert replaced_content.count(new_instaload) == 1

        assert content.count(old_glyph) == 1, f'cannot find current Magic Glyph in {dst_filename}'
        replaced_content = content.replace(old_glyph, new_glyph)
        assert replaced_content.count(new_glyph) == 1

        replaced_contents.append(replaced_content)

    if old_instaload == new_instaload:
        print('Insta-Load code is already up to date')
        return

    for i, dst_filename in enumerate(dst_filenames):
        Path(dst_filenames[i]).write_text(replaced_contents[i])
        print(f'Code replaced in {dst_filenames[i]}')
    print(f'Insta-Load replaced: {len(old_instaload)} characters -> {len(new_instaload)} characters')


if __name__ == '__main__':
    src_filename = 'wat/inspection/inspection.py'
    dst_filenames = ['README.md']
    _regenerate(src_filename, dst_filenames)
