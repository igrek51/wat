# 🙀 WAT

<div align="center">
    <a href="https://github.com/igrek51/wat">GitHub</a>
    -
    <a href="https://pypi.org/project/wat">PyPI</a>
    -
    <a href="https://igrek51.github.io/wat">Documentation</a>
</div>

Deep inspection of Python objects.

**WAT** is a powerful inspection tool
designed to help you explore unknown objects and examine them at runtime.

> "Wat" is a variant of the English word "what" that is often used to express confusion or disgust

If you ever find yourself in a Python console, feeling lost and confused,
and wondering "WAT? What is this thing?",
that's where `wat` inspector comes in handy.

Launch the Python Interpreter and execute `wat / object` on any `object`
to investigate its
**type**, **formatted value**, **variables**, **methods**, **parent types**, **signature**,
**documentation**, and its **source code**.
This makes it particularly useful for debugging or understanding intricate data structures in Python,
providing a straightforward way to answer "what" exactly an object represents.

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-datetime-now.png?raw=true)

<video width="100%" controls="true" allowFullscreen="true" src="https://github.com/user-attachments/assets/022ef89a-9e35-45be-9e2f-08d2c6af9075" poster="https://raw.githubusercontent.com/igrek51/wat/master/docs/img/wat-set.png">
</video>

Alternatively, use `wat(object)` syntax for the same in-depth inspection.

## Loading

### Insta-Load
If you want to quickly debug something,
you can use this inspector **without installing anything**, in the same session.

Load it on the fly by pasting this snippet to your Python interpreter:
```python
import base64, zlib
code = b'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'
exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
```

Now you can use `wat` object.

> [!Warning]
> Before executing **Insta-Load** snippet, it's recommended to verify what you're about to run.
> You can either:
>
> - Verify what's inside the extracted code beforehand:
>   ```python
>   print(zlib.decompress(base64.b64decode(code)).decode())
>   ```
> - Paste the content of [inspection.py](https://github.com/igrek51/wat/blob/master/wat/inspection/inspection.py) into your interpreter.
>   It has the same effect.
> - [Install package with pip](#install-with-pip) and review the code.

### Install with pip
Alternatively, install **wat** package and import inspection tool from **wat** module:
```sh
pip install wat
```
```python
import wat
```
This package has no external dependencies.

### Load from Unicode Glyph
Fun Fact: You can load WAT from a single Unicode glyph.
```python
import zlib
glyph = '🙀󠅸󠆜󠇕󠅛ⷽ󠅮󠇛󠇈󠄑﻿󠄿󠅏󠅁󠆤󠅿󠆐󠇌󠇩󠇔󠇤󠆮󠄟󠆀󠇯󠆘󠇖󠅉󠅼󠇗󠆠󠆹󠆸󠅰󠆜󠄻󠄔󠆶󠅁󠅐󠇢󠇊󠇦󠆙󠄢󠄅󠆒󠆊󠆭󠄊󠄂󠇮󠄡ⷺ󠄌󠅽󠆰󠅻󠆒󠇎󠇇󠅾󠆓󠆔󠆜󠇋󠄕󠅭󠄍󠅘󠄢󠅷󠅷󠅾󠄻󠄳󠄻󠄻󠄳ⷻ󠆡󠅅󠅓󠄯󠆃󠄼󠇫󠆲󠅹󠆙󠆵󠆭󠅨󠆃󠅢󠆹󠆪󠆛󠇎󠄔󠄽󠆒󠄅󠅅󠇕󠆮󠇄󠆼󠅓󠆯󠆵󠆮󠅨󠆄󠅺󠅪󠄷󠇭󠆣󠄅󠇢󠅵󠆛󠅕󠅑󠅝󠄫󠆨󠇣󠅪󠄳󠄉󠅎󠅗󠅝󠅑󠅗󠅙󠄹󠄉󠇎󠄷󠄫ⷱ󠇨󠇏󠄆󠆟󠄾󠆃󠇗󠄌﻿󠆲󠆮󠄖󠇅ⷵ󠇑󠆣󠄀ⷾ󠇚󠄛󠆠󠄾󠄊󠅦󠅵󠅝󠇒󠅻󠆾󠆮󠅲󠇑󠅘󠄅󠅕󠆝󠇗ⷳ󠇖󠄪󠄨󠇫󠇪󠇚󠅺󠆝󠇗󠆹󠆰󠅟󠆳󠆲󠇔ⷴ󠅣󠄌󠄜󠅷󠅝󠅓󠇌󠇖󠆝󠅠󠄞󠆪󠅬󠄉󠄐󠅭󠇗󠇐󠇛󠆇󠆬󠅜󠇃󠄫󠄈󠅄󠆯󠄠󠄦󠆼󠆑󠄼󠄊󠄿󠆛󠆕󠅢󠄟󠇋󠆫󠆦ⷸ󠆐󠅵󠅶󠆓󠆶󠆸󠆮󠆲󠅮󠇝󠅀󠆙󠇒󠇑󠄅ⷴ󠅷󠇅ⷴⷵ󠇜󠄯󠇎󠇅󠅂󠆍󠅅󠆺󠆨󠆛󠅥󠇖󠅅ⷵ󠇬󠇇󠅉ⷰ󠅤󠇂󠄊󠅋󠆾󠇉󠇊󠅖󠅌󠅤󠇗󠇪󠆍󠅕󠆥󠇞󠅐󠅏󠇪󠄙󠆕󠆤󠆟󠅉󠅃󠇪󠄍󠅞ⷸ󠄱󠄾󠆒󠇪󠇄󠆱󠅉󠆜󠆑󠆊󠆸󠅏ⷺ󠇔󠅽ⷲ󠅗󠅐󠄷󠄈󠆡ⷻ󠇦󠄯󠇙󠄹󠅾󠇨󠄆󠇄󠄂󠅾󠆘󠄒󠅦󠆄󠆿󠅤󠅩󠅌󠅌󠇔󠇫󠅮󠆵󠇮󠆒󠆲󠅨󠆻󠄨󠇝󠄔󠆢󠇌󠅓󠆥󠆍󠆲󠆨󠅄󠇋󠇊󠅠󠅖󠅣󠄦󠄩󠄖󠅨󠆙󠇓󠆶󠇋󠆁󠅸󠅚󠆴󠅙󠇗󠅭󠄢󠄩󠄓󠄍󠆣󠅨󠆖󠄅󠇨󠄷󠆽󠄫ⷲ󠇮󠄦󠆩󠇛󠇩󠆵󠇨󠅒󠅝󠇚󠄖﻿󠄐󠅑󠄼󠆝󠇗󠇥󠅺󠅙󠆵󠆚󠆊󠄙󠆙󠅂󠇧󠆢󠇩󠆢󠆧󠆠ⷽ󠅮󠅓󠆊󠇩󠆋󠇣󠆳󠇠󠆳󠄠ⷼⷹ󠆟󠄿󠆅󠇁󠄓󠄏󠄚󠄪󠇎󠅎󠇞󠆝󠆜󠇇󠄾󠅈󠆶󠅚󠆉󠄪󠆏󠄾󠄖󠆡󠄑󠅠󠄷󠅕󠄐󠅞󠅖󠇡ⷴ󠇇󠆺󠆨󠆢󠄈󠅕󠄐󠆀󠅕󠄄ⷴ󠅐󠅔󠆲󠄃󠅔󠄁󠆗󠆴󠄰󠄚󠅝ⷰ󠆶󠆮󠄄󠄨󠄇󠅍󠇩󠆠󠄎󠆏󠆔󠄎ⷹ󠅽󠄪󠅧󠆑󠄖󠆁󠇨󠄃󠆚ⷶ󠇩󠆵󠆨󠅄󠄃󠇦󠆝󠅲󠄣󠅀󠅝󠇔󠄑ⷳ󠄊󠆶󠆛󠇒ⷴ󠅉󠆤󠇕ⷲ󠄛󠅷󠅅󠄦󠅱󠇞󠆬󠆅󠆒󠅫󠆥󠄚󠇣󠄣󠆶󠇑󠄣󠅩󠇪󠆂󠄤󠅁󠅔󠆪󠅅󠄓󠅱󠅫󠅒󠆨󠄪󠅖󠄩󠆌󠅚󠇝󠅄󠆺ⷳ󠆸󠇇󠅷󠆸󠅥󠆭󠆟󠆟󠄝󠆿󠄾󠇟ⷱ󠄄󠇟󠆒󠆎󠅷󠇁󠅖󠇓󠇭󠅂󠆢󠄓󠄰󠄙󠄎󠄠󠄀󠇉󠄸ⷽ󠄨󠄕ⷲ󠅮󠆓󠅡󠇍󠅟󠅎󠆎󠅟󠇭󠆶󠅆󠆪󠆝󠆬󠄏󠆵󠄾󠇑﻿󠅨󠅵󠇢󠅋󠅄󠄟󠆨󠄐󠇖󠇗󠅠󠅟󠇤󠆵󠄜󠄖󠆱󠅄󠇂󠆮󠆲󠅆󠅔󠅝󠆛󠆄󠆓󠅀󠇚󠅔󠆊󠆓󠆁󠆋󠆩󠅡󠅫󠅵󠆢󠅇󠅅󠆒󠄝󠇐󠆍󠅪󠆥󠄻󠆗󠄅󠆲󠅯󠆴󠄱󠇩󠅂󠄣󠇨󠄔󠆦󠅩󠇃󠇦󠄑󠆦󠅩󠄩󠆪󠄴󠄅󠆦󠇘󠅲󠆭󠆹󠇛󠅬󠇌󠇋󠅨󠇇󠅀󠅭󠄺󠅵󠇭󠄏󠆪󠅘󠄖󠅫󠆈󠇄ⷽ󠅜󠆬󠄺󠅲󠇬󠄧󠅍󠅓󠄷󠅮󠄏󠄫󠆌󠄙󠄾󠆿󠄈󠅡󠆚󠅡󠇔󠅈󠅼󠄑󠆰󠆐󠅤󠄈󠅿ⷾ󠇩󠅟󠆡ⷱ󠄁󠄺󠄀󠄤󠆤󠅪󠄅󠆙󠇪ⷲ󠄈󠄩󠄧󠆁󠆞󠄅󠇣󠆶󠆧󠅃󠆉󠄙󠅞󠅕󠄤󠇅󠄃󠄗󠇌󠇝󠇀󠇃󠇠󠇜󠄃󠆡󠆠󠄪󠇈󠆪󠄼󠆈󠇐󠅕󠇈󠅙󠇏󠇎󠄻󠆦ⷲ󠄑󠆡󠆙󠄒ⷼ󠇤󠆺󠇪󠄢ⷴ󠅉󠄱󠇎󠇃󠆧󠅻󠆇󠇧󠇕󠇩󠇋󠅷󠆻󠇇󠆏󠄟󠅯󠆁󠆒󠆾󠅭󠄓󠇯󠇏󠄸󠄋󠄁ⷽ󠇍󠅅󠄏󠄇󠆴󠄋󠅈󠄓󠇨󠇀󠄂󠆻ⷲ󠄽󠄘󠅆󠄚󠄒󠅐󠅺󠄽󠆈󠄉󠆔󠄃󠅨󠅗󠇢󠅈󠅨󠆉󠇘󠇖󠇫󠅦󠄮󠇇󠆉󠆟󠅓󠄄󠆋󠆜󠆡󠇁󠅰󠅃󠅵󠄏󠄰󠅌󠅮󠇈󠆉󠆊󠅤ⷷ󠆲󠇚󠅲󠆩󠆙󠄕󠇖󠄸󠅰󠅎󠆤󠆁󠄳󠆕󠆭󠆴󠅉󠄋󠄕󠄢󠆏󠇒󠄂󠄢󠅆󠅪󠇊󠄝󠅟󠄾󠄉󠅮󠇅󠄦󠄩󠆳󠇥󠄬󠇏󠆈ⷶ󠆈󠄾󠆧󠅨󠅠󠄽󠇛󠄢󠆏󠄎ⷳ󠄳󠆗󠅸󠅭󠇚󠆂󠆮󠄠󠄓󠆉󠄌󠆺󠅆󠇦󠅘󠆲󠆯󠅯󠅦󠄚󠅣󠄓ⷰ󠆀󠆡󠄩󠄯󠄚󠇏󠆂󠅤ⷺ󠄀ⷵ󠄐󠆬󠆳󠆦󠅫󠇯󠆊󠇮󠄦󠆂󠆩󠄓󠆲󠇡󠅡󠄅ⷰ󠅣󠄕󠄻󠇆󠇇󠅙󠆇󠅯󠆹󠅜󠄜󠆻󠆃󠄁󠅵󠅝󠅑󠆭󠆅󠄮󠆔󠅹󠅙󠆿󠅯󠇙󠄵󠄡󠅊󠆨󠅱󠇧󠇃󠄱󠇋󠆙ⷸ󠄀󠄘ⷻ󠆎󠇥󠅅󠇖󠆊󠄓󠅺󠄄󠅭󠄆󠅙󠄛󠆈󠄡󠄘󠇃󠆜ⷶ󠄉󠆉󠄶󠅌󠆎󠅦󠄟󠇡󠅃󠆀󠆏󠄉󠄃󠇇󠆨󠄬󠇝󠆄󠅦󠄘󠆹󠅕󠄳󠄌󠆶󠆏󠄠󠄒󠇩󠄥󠆤󠅆ⷱⷹ󠄠󠄈󠄛󠆑󠆟󠅔󠆓󠄫󠅋󠄌󠄯󠆉󠆄󠆧󠅈󠅆󠅱󠆅󠅙󠆜󠇨󠄩󠆘󠇨󠅎󠆼ⷴ󠅲󠆢󠇇󠅌󠅾󠅏󠄬󠄭󠇨󠄧ⷲ󠄇󠄉ⷼ󠅋󠄋󠄽󠇨󠅡󠅹󠄤󠆜󠆑󠅍󠄭󠅜󠄘󠅖󠇥󠄴󠄌󠆵󠄉󠆸󠅲󠆀󠆣󠇯󠅑󠄊󠆊󠄝󠄓󠄓󠅆󠇢󠅁󠇈󠄰󠆂󠅰󠄐󠇫󠆹󠄾󠇤󠆒󠆎󠄬󠄳󠄕󠆋󠇢󠄾󠄉󠅹󠇉󠆢󠆒󠄒󠆗󠆬󠅮󠄠󠇩󠆃󠄴󠅮󠆱󠆮󠅸󠆺󠄎󠅃󠅤󠇭󠆦󠆚󠄇󠆨󠆔󠅁󠄘󠆇󠄚󠅽󠆢󠆩󠅚󠆊󠇮󠆦󠇎󠄇󠄪󠅦󠇫󠆢󠆄󠆞󠅵󠇍󠅍󠇖󠄎󠅅󠇀󠄁󠅦󠅬󠄶󠅬󠆇󠆯󠇪󠅃󠄻󠇟󠇕󠄾ⷴ󠆯󠄧󠅿﻿󠇡ⷴ󠄌󠆒󠄤󠅮󠆶󠆓󠇅󠄯󠆏󠇟󠆼󠄹󠅾ⷱ󠇦󠅤󠆷󠇅󠄎󠅕󠇩󠆻󠇗󠇟󠆾󠄽󠄾󠅿󠅿󠄆󠇅󠅆ⷻ󠄦󠆧󠇒󠇖󠇡ⷻⷵ󠄁󠆃󠆐󠅼󠄨󠇁󠆁󠆊󠆉󠅌󠄜󠅐󠅶󠅰ⷺ󠇎󠄷󠆂󠄉󠇌󠆉󠄜󠆒󠆞󠄌󠆕󠇋󠅦󠇡󠅹󠄀󠄭󠇥󠄢󠄫󠅊󠆑󠄇󠅝󠄝󠅀󠄏󠆁󠄝󠄪󠆂󠄭󠇍󠄕󠄑󠇯󠇠󠅑󠇘󠇜󠄻󠅡󠅝ⷲ󠆎󠄳󠇀󠇢󠅕󠄶󠅱󠇂󠄽󠆬󠄋󠅰ⷶⷶ󠆘󠇐󠅓󠅚󠇎󠆢󠄩󠅥󠇕󠆑󠆳ⷼ󠄠ⷺ󠄅󠅵󠇈󠅾󠄠󠆥󠄠󠄅󠄉󠄛󠄶󠆮󠆮󠄣󠄳ⷻ󠆬󠅨󠄂󠇩󠅗󠅓󠆐󠄫󠇃󠄷󠄯󠅊󠆐󠄓󠅀󠅲󠅯󠆱󠅀󠇁󠅪󠇌󠄣󠄍󠅄󠅋󠇚󠄏󠇐󠄲󠅙󠆨󠄞󠆇󠆺󠄦󠇖󠇫󠅺󠆧󠅷󠇒󠄶󠅵󠆎󠅏󠆱󠅫󠆌󠆁󠅊󠇘󠆿󠄿󠄾󠅻󠇍󠅶󠆧󠆃󠆪󠄶󠇉󠇓󠅗󠄧󠄻󠄹󠅬󠆈󠆼󠄋󠆒󠅠󠆫󠅻󠅕󠄃󠇨󠅱󠇕󠆉ⷻ󠅎󠆅󠇍󠆢󠅩󠅹󠅱󠄶󠄉󠇒󠄉ⷴ󠇝󠅶󠄉󠅖󠅏󠄡󠆃󠇮󠄊󠆚󠆧󠆔󠅱󠆙󠅕󠅒󠇛󠇡󠄌󠇄󠇬󠇖󠅙󠄉󠄙󠆠󠄸󠄎󠆞󠄇󠇏󠆞󠄾󠇭󠄛󠆞󠅮󠅲󠅱󠄄ⷵ󠅗󠅪󠇍󠅉󠆋󠅒󠇈󠅜󠄟󠄍󠆶󠇭󠄏󠆰󠅴󠄓󠄃󠇃󠄫󠄇󠆉󠆴󠅤󠅲󠇖ⷾ󠄄󠄀󠇍󠄚󠅍󠆺󠅮󠆒󠇊ⷷ󠄤󠆪󠅎󠅚󠆪󠄚󠄟󠇈󠅍󠅻ⷽ󠄚󠄷󠄑󠇘󠅹󠇦󠅯󠅤󠄵󠇦󠆬󠄏󠅈󠅘ⷷ󠇀󠄞󠅡󠆲󠇧󠄤󠆰󠅐󠆠󠆱󠄯󠄫󠄿󠄣󠅶󠇁ⷷ󠄀󠅋󠆃󠅲󠄦󠆏󠄽󠅯󠄰󠇟󠆟󠆀󠄃󠅃󠅏󠆔󠄼󠄵󠇃󠅒󠆴󠇠󠄨󠆺󠆬󠆚󠇫󠇦󠄸󠄩ⷺ󠅝󠄾󠅖󠅎ⷵⷼ󠅬󠄗󠅮󠇥󠄒󠅗󠆲ⷺ󠅘󠆁ⷱ󠅚󠅼󠇌󠆵󠅨󠄯ⷾⷶⷴ󠇭󠇉󠄎󠆛󠄸󠆢󠇚ⷴ󠇈󠇭󠄸ⷽⷹ󠇙ⷻ󠆓󠄝󠄶󠄙󠆥󠆧󠅍󠆬󠅱󠆀󠅯󠆎󠇟󠆼󠄻󠇙󠅑󠄣󠄟󠆢󠆯󠄏󠄈﻿󠄝󠆬󠄯󠇊󠄺󠇫󠇢󠄁󠇅󠅨󠆡󠇞󠅿ⷷ󠇢󠇤󠅬󠆷󠄝󠅘󠆹󠄏󠇂󠇦󠇅󠆼󠇫󠇃󠆩󠄁󠇄󠇚ⷾ󠄨󠆪󠄁󠆄󠆉ⷹ󠄬󠄞󠆇󠇆󠆭󠆲󠅱󠅨󠆬󠅽󠄈󠆴󠇜󠇊󠆠󠄌󠇈󠅊󠄾󠆳󠇪󠄚󠄒󠆩󠅙󠆓󠇍󠅯󠄡ⷺ󠄀󠇠ⷼ󠄦󠅩󠇄󠅴󠆱󠄮󠅋󠅺󠆉󠇂󠆯󠆣󠇩󠆓ⷸ󠅹󠄸󠅑󠄈󠆚󠇓󠄁󠇒󠅱󠅽󠆒󠄃ⷽ󠆺󠇯󠅨ⷻ󠄘󠇓󠅫󠇈󠅿󠅖󠇑󠆳󠇘ⷱ󠆽󠇏󠆝󠄡ⷰ󠇑󠇑󠆌󠇕󠅦󠆍󠆗󠄒ⷴ󠅇󠄀󠄞󠅝󠄥󠅙󠇓󠆇󠆕ⷶ󠄼ⷸ󠅲󠇀󠆭󠆺󠇦󠅶󠅲󠅶󠅶󠅺󠅶󠄄󠇁󠆽󠆆󠄜󠅌󠆬󠇊󠅍󠅐󠆁󠇏󠄖󠆹󠅯󠄪󠇨󠇚󠇐󠆋󠅃󠆯󠅻󠇌󠆍󠅤󠇜󠅮󠅷󠆞󠆥󠅵󠅢󠇙󠄦󠆸󠅊󠅶󠄽󠇁󠆭󠇇󠄿󠅆󠄦󠇏󠅗ⷸ󠄭󠅂󠅞󠆹󠅁󠇚󠇎󠅋󠆷ⷹ󠆔󠇀󠆣ⷸ󠇊󠅡󠇔󠆉󠆷󠇔󠆂󠇢󠆨󠇙󠅍󠆢󠆲ⷸ󠆐󠄜󠅒󠆊󠆭󠅆󠅰󠇆󠇒󠆓󠆒󠆶󠄬󠄓󠅫󠄓󠄴󠇄󠅒󠇜󠄻󠇕󠄶󠄌ⷸ󠅅󠆷󠆛󠆰󠄐󠄅󠆞󠅥󠄰󠅳󠄪󠅫󠆯󠅰󠄃󠆔󠅼󠆡󠆦󠆍󠄤ⷱ󠇧󠅪󠄂󠇬󠅧󠄕ⷼ󠄶ⷱ󠆁󠄏󠄆󠅮󠆌󠅭󠇛󠆲󠆬󠄉󠅘󠆶󠇝󠅿󠇁󠆲󠇊󠄡ⷷ󠇠󠆊󠅹󠅱󠄵󠅤󠅗󠆽ⷰ󠇢󠄱󠅏󠇚󠆆󠅢󠅔󠄷󠅴ⷲ󠄟󠆰󠆔󠆋ⷽ󠆆󠅲ⷵ󠄿󠅣󠄧󠄗󠄏󠄷󠆓󠆫󠅁󠄫󠇑󠆻󠆻󠆩󠄜󠆫󠅥󠆝󠆯󠅋󠅞󠄳󠆧󠇓󠄴󠇥󠇗󠄴󠅕󠄺󠇦󠅷󠄕󠅼󠄱󠄕󠆔󠄥󠆼󠅩󠄎󠄔󠆴󠆄󠅌󠅭󠇚󠅃󠇮󠅅ⷵ󠇅󠇋󠆸󠇝󠅞󠆏󠇊󠄔󠆌󠆼󠆛󠆎󠆒󠇪󠅵󠅋󠅯󠆃󠄹󠄵󠆶󠆯󠆖󠆑󠅔󠅌󠄋󠇉󠅥󠅓󠆻󠇫󠅈󠄚󠄯󠇐󠇥ⷽ󠄤󠆘󠅥󠆭󠄠󠄜󠄜󠄽󠅑󠆭󠆗󠅴󠄢󠄑󠅩󠅅󠄡󠆩󠆷󠄛󠄤󠇧󠇗󠄽󠇥󠆄󠆨󠄫󠄋󠆣󠇅󠅝󠄁󠅘󠄹󠆹󠄔ⷸ󠇗󠇛󠅃󠇂󠄿󠇞ⷶ󠅰󠅆󠅍󠆃󠇩󠄭󠆈󠆡󠅃󠄒󠆙󠇧󠄷󠆸󠄿󠆢󠅪󠄠󠆎󠇏󠅯󠅓󠄪󠆋ⷾ󠆠󠇣󠄦󠆽󠅛󠆢󠇣󠄫󠅢󠇘󠅫󠄼󠅝󠄘󠇑󠆓󠆳󠅏󠆦󠇫󠆦󠄋󠅘󠅟󠅖󠄎󠆘󠄑󠇁󠇛󠆨󠆔󠄧󠅱󠅈󠅱󠄔󠄸󠅣󠇜󠆇󠇛󠄝󠅙󠆅󠅨󠇮󠅕󠇝󠇏󠆓󠄝󠅆󠅰󠅑󠆛󠆢󠄾󠅡󠅉󠇣󠅯󠇔󠇥󠇂󠆚󠆳󠇃󠄤󠆱󠆳󠄬󠅽󠆈󠄜󠇢󠅾󠄅󠅋󠆤󠄖󠇖󠅍󠅦󠆫󠄜󠄑󠆕󠅉󠄾󠅴󠇛󠆓󠆙󠅝󠆭󠅧󠅥󠄱󠇇󠄕󠄭󠅸󠇅󠆌󠆌󠄱󠅃󠇫󠄳󠄄󠅺󠇉󠄳󠆕󠆛󠅕󠅦󠇝󠆒󠆩󠄝󠅊󠆻󠅈󠅭󠅑󠇉ⷰ󠄪󠆉󠄎ⷵ󠄰󠆈󠇮󠅁󠅱󠅧󠆇󠆑ⷼ󠇝󠇔󠄾󠅏󠄬󠄴󠆯ⷲ󠄾󠅙󠅮󠄃󠇯󠅊󠅼󠄘󠇞󠆅ⷶ󠅱󠆤󠆸󠄏󠆁󠆱󠄤ⷶ󠅑ⷰ󠆄󠇋󠆌󠄱󠅺󠄈󠅗󠅺﻿󠇜󠄫󠄜󠄽󠇮󠆣󠅃󠆽󠆿󠄑󠆱󠇅󠇀󠅑󠅯󠅺󠄐󠆗󠅐󠆏󠆌󠅚󠅝󠄏󠇍󠇔󠄇󠇬󠆪󠇘󠆳󠇎󠄖󠄄󠅥󠄝󠆓󠅤󠅐󠆚󠄁󠆶ⷶ󠄐󠄞󠇜󠄎󠇐󠇊󠆵󠇬󠆛󠆴󠇫󠆎ⷾ󠇇󠆪󠅗󠇙󠇃󠅃ⷵ󠅫ⷵⷾ󠅫󠄨󠇘󠄖󠆆󠄴󠄼󠄦󠇍󠅡󠄕󠄟󠆦󠅼󠆰󠆎󠆝󠇣󠄐󠆞󠆆󠆖󠄯󠅀󠆭󠆻󠅳󠆥󠅷󠅔󠅾󠅀󠇫󠆯󠄤ⷰ󠄃󠆕󠅮ⷵⷽ󠄫󠇨󠇜󠆖󠄄󠅅󠅳󠅅ⷹ󠄈󠆍󠄟󠄦󠄼󠆬󠅰󠆊󠄠󠄃󠄡󠄼󠄗󠆫󠇮󠇆󠄉ⷴ󠄪󠅢󠇏󠇗󠄍󠆦󠄿󠇜󠆌󠄅󠅃󠆦󠅒󠇤󠆨󠆁󠄵󠆮󠅋󠄫󠅥󠆦󠇖ⷶ󠆍󠄎󠆗󠅛󠇮󠆁󠄾󠆧󠆋󠅴󠄆󠅬󠄸󠆉󠄚󠆖󠄻󠆱󠅎󠄩󠆹󠆍ⷴ󠇓󠄤󠇨󠆊󠆮󠄔󠇎󠅦ⷲ󠇐󠇐󠅯󠆩󠇙󠇎󠄝󠅰󠄔󠆠󠄢󠄎󠆫󠅀󠆞󠅍󠅪󠇠󠇩󠆭󠇘󠇀󠇚󠇑󠆒󠅧󠅬󠇇󠅗󠆓󠅜󠄠󠇖󠆕󠅤󠅅󠆓󠄍󠇯󠇔󠇊󠆃󠄤󠆇󠄲󠇮󠆟󠆝󠄏󠅬󠇜ⷾ󠆂󠄽󠅛󠅫󠅳󠇕󠇚󠆰󠆕󠅪󠅮󠇄󠆴󠅝󠇏󠆢ⷰⷲⷲⷾ󠇙󠇬ⷲⷲ󠇢ⷲ󠄲﻿󠄬ⷺ󠄊󠄿󠇣󠄿󠄭󠅱󠆭󠄃﻿󠅄󠄥󠄯󠆡ⷽ󠆐󠇉ⷼ󠇧ⷱ󠇣󠇇ⷲ󠇬󠆌󠅏󠅘󠅨󠅇󠄇󠆏󠄂󠇄󠅽󠆶󠇄󠆛󠄼󠇫󠇪󠆶󠆪󠇯󠄪󠆙󠆝󠆶󠄁󠄞󠅗ⷲ󠄅󠆰󠆠󠅞󠅡󠅾󠅙󠄷󠄭󠆀󠅰󠄐󠅄󠅆󠄡󠇏󠄬󠆺󠄴󠆍󠅚󠅑󠄮󠄦󠇁󠆓󠄧󠇪󠇆󠇏󠇭󠅝󠇖󠅜󠇛󠆳󠄝󠄛󠅌󠅓󠆷󠄺󠅱󠅟󠆽󠆶ⷲ󠅢󠇘󠅶󠄷󠆂󠅑󠅔󠇩󠆪󠆩󠆯󠄱󠇣󠇢󠄋󠅥󠄖󠅗󠅴󠆿󠆅󠆹󠅲󠇍󠄛󠆭ⷺ󠄮󠇫󠄆󠅑󠅜󠅋󠇧󠇎󠇀󠅗󠇂󠄂󠇢󠅆󠆔󠅶󠄞󠆨󠅮󠅈󠆅󠅖󠆏󠆸󠇏󠇓󠇫󠅐󠄵ⷼⷺ󠆇󠇣ⷳ󠇀󠅨󠆞󠆵ⷻ󠇜󠄢󠆷󠆺ⷱ󠄠󠅰󠄜󠆓󠅅󠅸󠇞󠅬󠆜󠄄󠄙󠅤󠄈󠅾󠄫󠆁󠅔󠆮󠄉󠇈󠅞󠆓󠄩󠄬󠆕󠆊󠅅󠄡󠇀󠅿ⷹ󠆍󠅡󠇐󠆥󠄊󠇀󠆵󠄹󠅴󠅎󠆻󠆩󠅳󠅯󠇨󠄻󠄅󠆧󠅐󠅠󠅽󠅵󠅴󠅙󠅩󠆓󠇇󠄝󠄯󠆾󠅌󠇐󠇧󠆉󠇫󠆬󠇮󠅯󠆊󠇜󠆎󠆦󠆁󠆙󠅛󠇤󠅬󠅕󠇀ⷰ󠇡󠇙󠆗󠅚󠄸󠆤󠄻󠅽󠅎󠆯ⷱ󠅼󠄺󠅌󠇄󠅻󠅔󠇖ⷱ󠅗󠅐󠅃󠆺󠄖󠆨󠄃󠇊󠆉󠇬󠆟󠇮󠅭󠇠󠄤ⷲ󠇡󠇐󠅣ⷴ󠇠󠆪󠆺ⷺ󠄼󠆛󠇍󠄚ⷱ󠆡󠆀󠄀󠆛󠆳﻿󠆑󠆱󠆣󠆞󠇃󠆢󠅑󠆞󠇐ⷹ󠅠󠅼󠆼󠇠󠇫󠇆󠄡󠄡󠇏󠆧󠆸󠅣󠅈󠅹󠆷󠆶󠄧󠄨󠇅󠄈󠄋󠄌󠄆󠇤󠄮󠇀󠅿󠄤󠆺󠆻󠄑󠄍󠅌ⷹ󠄛󠆡󠆆󠄟󠆱󠇯󠆲󠆖󠄯󠅇󠇦󠄾󠄘󠄔󠄺󠄖󠄳󠄯󠇗󠄸󠅪󠄥󠅮󠆿󠆰󠅳󠄜󠄐󠄇󠇌󠇞󠄢󠆒󠆓󠇀󠇪󠄒󠄴󠄳󠅪󠅰󠄽󠅫󠇪󠆚󠅡󠄬󠅹󠄇󠆑󠅏󠆵󠇈󠆙󠆉󠄬󠇇󠅁󠆤󠆡󠆀󠄲󠄟󠇩󠆺󠇉󠄶󠄖󠅔󠅞󠆴󠅴󠇉󠆀󠆜󠇬󠅢󠅝󠇪󠅋󠆍󠄌󠄏󠇞󠆧󠆭󠅋󠇑󠆷󠄢󠅨󠅭󠆡󠄈󠇔󠇂󠆼󠆇󠇒ⷶ󠅠󠅞󠆢󠇎ⷼ󠇩󠅙󠇖󠆠ⷵ󠅶󠅼ⷾ󠅆ⷱ󠇀󠅴󠄥󠆢󠇀󠅄󠆽󠄑󠇬󠇫󠆲󠆞󠅙󠇠󠄖󠄀󠇗󠅘󠄈󠆡󠇯󠄡󠆕󠄃󠄆󠆙󠅒󠅘󠅼󠅃󠆣󠄼ⷲ󠅶󠄷󠇈󠄯ⷵ󠇣󠆔󠅮󠅃󠆣󠅠󠆕󠆱󠆗󠅄󠄣󠄳󠇑󠄂󠆝󠄾󠄆󠆍󠅞󠆰󠇀󠆕󠄓󠆔󠄌󠆞󠅸󠄑󠅯ⷳ󠅺󠆵󠆉󠄴󠇡󠅔󠅊󠄖󠄑󠆢󠅵󠄱󠄆󠄯󠄟󠅰󠆛󠆇󠅂󠇭󠄹󠅱󠄛󠇟󠅅ⷹ󠇂󠇝󠄢󠆠󠄁󠇢󠆵󠆰󠅊󠆔󠅸󠆠󠅍󠅾󠅅󠄧󠇚󠅖󠅤ⷳ󠆙󠆒󠄁󠇁󠅤󠅏󠄆󠄓󠇂ⷻ󠄛󠇗󠄂󠅂󠆣󠅡󠆥󠄈󠅖󠅰󠄍󠄖󠅨󠆟󠆳󠆍󠄅󠄾󠄺󠆸󠄳󠄑󠇇󠆿󠅿󠄤󠄯󠅇ⷻ󠇗󠇃󠄑󠄜󠅇󠅯󠄨󠆲󠇇󠄃󠄀󠄩󠄋󠆘󠅰󠅻󠆘󠅾󠆫󠄲󠇛󠆤󠅜󠄗ⷱ󠆗󠅋󠄆󠇚󠅲󠄨ⷻ󠆛󠅥󠅒󠅥󠅎󠄫󠄟󠇂󠅎󠄦󠅰󠄓󠄫󠄊󠆡󠄝󠄤󠅈ⷶ󠄝ⷴ󠄡󠅌󠄔󠅯󠅨󠅼󠆜ⷻ󠅈󠄋󠆼󠅄󠅝󠅺ⷺ󠄚󠅕󠆳󠆛󠆥󠆐󠇡󠆩󠆼󠆩󠄷󠄅󠄪󠅱󠆧󠄲󠄠󠅇󠄂󠆢󠄲󠅺󠆲ⷳ󠅡󠇆󠆐󠄭󠅺󠅻󠆑󠆪󠇕󠅖󠇊󠄟󠇂󠇜󠇅󠄯󠅴󠆋ⷸ󠅍󠆓󠄸󠇜ⷵ󠄕󠅢󠄸󠇡󠆜󠄷󠆑ⷽ󠆬󠇪󠅕󠇤󠅞ⷱ󠇃󠆖󠅞󠆆󠄷󠅤󠄜󠆾󠄌󠅽󠆲󠇩󠅺󠆕󠇣ⷶ󠆪󠅯󠅌󠇘󠄒󠆴󠆛󠅀󠅂󠄋󠅓󠆶󠅏󠇗󠅫󠆩󠆳󠅈󠄣󠆄󠆟󠆜󠇉󠆖󠇆󠅉󠅹󠆖󠄩󠆧󠄒󠇛󠅧󠄯󠆗󠅼󠆀󠆧󠆔󠇓󠇇ⷱ󠆕󠆾󠆹󠄏󠇚󠄩󠄏󠇐󠆐󠆝󠄺󠅶󠇯󠆹󠅜󠄟󠆺󠅷󠇧󠆆󠇖󠆑󠄎󠇃ⷽ󠄴󠆹󠇏󠄌󠆛󠇇󠅞󠅶󠄜󠄯󠄲󠄈󠄢󠅭󠅭󠄏󠆆󠆙󠄢ⷸ󠄧󠆪󠄏󠇌󠅪󠆲󠄍󠄗󠅘󠄓󠄞󠄅ⷲ󠅧󠄤󠅡󠄇󠆽󠇁󠄫󠅶󠆺󠄣ⷴ󠆺󠆝󠅂ⷻ󠆢󠆩󠄫󠇮󠄌󠅲󠇮ⷴ󠇥󠇩󠆛󠇓󠄳󠅚󠄑󠇅󠄐󠅬󠇯󠅄󠄓󠇅󠆎󠇒󠅵󠄇󠇣󠄫󠅞󠇉󠆘󠅮󠇩󠄫󠅶󠇠󠅇󠄠󠅾󠅞󠅯󠇜󠄸󠄛󠆓󠆿󠄔󠆶󠅔󠅁ⷷ󠄨󠄆󠄧󠄍󠇉󠆄󠇕󠅚󠆁󠆆󠆈󠇎󠆠ⷸ󠇇󠄫󠄏󠅝󠅷ⷻ󠆿󠄖󠅉ⷶⷽ󠇞󠆃󠄺󠄘ⷹ󠆹󠆇󠆯󠆎󠅃󠇞󠆝󠄓󠄁󠄜󠆽󠆼ⷸ󠆠󠅳󠄁󠄿󠅔󠇙󠅨󠄪󠆨󠅱󠄛󠄋󠄤󠇋ⷳ󠅏󠄃󠄨󠇛󠆛󠅢󠇑󠅽󠄚󠅆ⷳ󠄫󠅠󠇔󠇍󠄧ⷲⷰ󠆩󠄀󠇥󠄧󠄊󠄠󠄯󠄧󠅫󠄐󠆊󠄋󠅮󠄰󠅃󠆿󠅭󠄒󠄮󠅧󠄖󠆚󠇐󠅄󠅫󠅇󠄊󠅎󠅾󠄤󠇒󠄎󠇝󠆝󠄖󠄗󠆒󠇤󠇊󠇍󠅡󠄨ⷳ󠄳󠆰󠅲󠇚󠆄󠆼󠅈󠇤󠅨󠆗󠄋ⷼ󠇦󠆕󠄗󠆕󠅐󠅞󠆇󠅏ⷰⷰ󠇐󠇞󠄹󠄠󠇮󠇫ⷺ󠄣󠆂󠆭󠄗󠆳ⷶ󠆃󠄧󠅉󠄐󠅲󠅖󠄙ⷾ󠅿󠆥󠆩󠅽󠄱󠇤󠅊󠇥󠆗󠇊󠇁󠇤󠆮󠄠󠄒ⷲ󠄓󠄤󠆱󠅐󠅁󠆔󠅯󠆽󠄥󠇓󠆨󠄬󠄰󠅾󠇡󠇨󠅚󠅣󠇏󠇢󠆢󠇉󠄊󠅠󠅐󠇟󠅨󠆧󠄫󠆼󠅣󠆙󠄊󠅯󠇪󠆽󠇃󠇥󠄞󠆃󠆼󠄸󠄾󠄃ⷷ󠅽﻿󠅬󠅶ⷱⷴ󠆫󠄯󠅿󠆷󠇤󠇥󠄜󠆝󠅌󠇊󠇢󠅧󠆦󠄘ⷷ󠅱󠅌󠇩󠄟󠅥󠄩󠆬󠅭󠄍󠇂󠄗󠆲󠆐󠅯󠆛󠆙ⷲ󠅧󠆪ⷼⷴ󠇭󠆉󠄩ⷽ󠆽󠇮󠇯ⷽ󠆉󠄁󠅖󠄘󠅴󠅹󠇄󠄔󠄫󠄈󠆼󠆘󠄨󠅋󠆿󠄰󠅜󠇈󠆛󠇗󠅽󠅙󠇔󠇝󠇫󠄾󠆾󠆾󠅿󠇝󠅧󠅟󠇭󠆿󠄚󠆢󠄯󠄕󠄜󠆬󠆑󠅍󠅻󠅕󠇚󠇛󠇏ⷴ󠅮󠄂󠇌󠅯󠇖󠇕󠄭󠅎󠇪󠅅󠅑󠅶󠆐󠅉󠇠󠅯󠅭󠇁󠅝󠆎󠅥󠄝󠇯󠅤󠇚󠄁󠆁󠆰󠆀ⷲ󠅉󠄘󠅻󠄙󠄏﻿󠄺󠆀󠅿󠆥󠆊󠇐󠇪󠆸󠅙󠅑󠄤󠆡󠅫󠇧󠆭ⷼ󠄁󠆈ⷱ󠆰󠆐󠄦󠆯󠄰󠆥󠇁󠅟󠄦󠆑󠄴󠅼󠇚󠆼󠄄󠅂󠅚ⷵ󠄫󠄙󠅁󠅀󠇚󠄜󠅈󠇈󠅦󠇀ⷷ󠆪󠄜󠄺ⷾ󠄷󠆔󠆺󠇁󠆈'
exec(zlib.decompress(bytes(ord(c)&255 for c in glyph[1:])).decode(), globals())
wat / 'WAT is going on?'
```

## Usage & modifiers
`wat` can quickly inspect things
by using the division operator (for faster typing without parentheses). 
A short syntax `wat / foo` is equivalent to `wat(foo)`.

You can call `wat.modifier / foo` with the following **modifiers**:

- `.short` or `.s` to hide the attributes (variables and methods inside the object)
  and print only value, type, parent types, signature and documentation
- `.dunder` to display dunder attributes (starting with double underscore)
- `.long` to show non-abbreviated values and docstrings
- `.code` to reveal the source code of a function, method, or class
- `.nodocs` to hide documentation for functions and classes
- `.caller` to show how and where the inspection was called (works in files, not REPL)
- `.public` to show only public attributes (hiding private attributes)
- `.all` to include all available information
- `.ret` to return the object back after the inspection
- `.str` to return the output string instead of printing it
- `.gray` to disable colorful output in the console
- `.color` to enforce colorful outputs in the console

You can chain modifiers, e.g. `wat.short.str.gray / 'foo'`.

Call `wat.locals` to inspect local variables.  
Call `wat.globals` to inspect global variables.

You can explore any object.
In Python, an "object" refers to not only to data structures,
but also to functions, classes, modules, built-in types, and more.

Type `wat` in the interpreter to learn more about this object itself.

There are several alternative syntaxes that are equivalent.
Choose the one that works best for you:
```python
wat.short / 'foo'  # fast typing
wat.short('foo')
wat('foo', short=True)  # natural Python syntax
'foo' | wat.short  # Unix piping
```

## Use Case Examples

### Determine type
In a dynamic typing language like Python, it's often hard to determine the type of an object.
WAT Inspector can help you with that by showing the name of the type with the module it comes from.

```python
>>> wat.short / (1,)
value: (1,)
type: tuple
len: 1
```

```python
>>> wat.short / {None}
value: {None}
type: set
len: 1
```

```python
>>> wat.short / user
str: admin
repr: <User: admin>
type: django.contrib.auth.models.User
parents: django.contrib.auth.models.AbstractUser, django.contrib.auth.base_user.AbstractBaseUser, django.contrib.auth.models.PermissionsMixin, django.db.models.base.Model, django.db.models.utils.AltersData
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-short-types.png?raw=true)

Now that you've identified the actual type,
you can put the type annotations in your code to reduce further confusion.

### Look up methods
By listing out methods with their signatures and docstrings, you can easily grasp how to use the unknown object.

```python
wat / ['foo']
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-list.png?raw=true)  
![](https://github.com/igrek51/wat/blob/master/docs/img/wat-set.png?raw=true)

Use `wat.long` if you want to see full doscstrings.

### Discover function's signature
See the docstrings and the signature of a function to learn how to use it.

```python
wat / str.split
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-str-split.png?raw=true)

### Look up attributes
List the attribues and their types to see what's really inside the inspected object.
```python
wat / re.match('(\d)_(.*)', '1_title')
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-re-match.png?raw=true)

### Explore modules
Another use case is to explore modules.
You can list the functions,
classes and sub-modules of a selected module.

```python
import pathlib
wat / pathlib
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-pathlib.png?raw=true)

Then, you can navigate further, e.g. `wat / pathlib.fnmatch`.

### Explore dunder attributes
By default, WAT Inspector hides attributes starting with `__`. Use `wat.dunder` to see them.
```python
wat.dunder / {}
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-dunder-dict.png?raw=true)

### Review the code
Look up the source code of a function to see how it really works.

```python
import colorsys
wat.code / colorsys.hsv_to_rgb
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-code-wat-call.png?raw=true)

### Prettify unreadable collections
Nested dictionaries and lists get nicely formatted, indented output:

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-nested-dict-pretty.png?raw=true)

### Debug with breakpoint
You can use Python's `breakpoint()` keyword to launch an interactive debugger in your program.
Attach to the interpreter and inspect things on the spot.

```python
(Pdb) import wat  # or paste Insta-Load snippet
(Pdb) wat / foo  # inspect local variables
...
(Pdb) c  # continue execution
```

### Look up local variables
Use `wat.locals` or `wat.globals` to look up the local and global variables respectively.

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-locals.png?raw=true)

### Learn Python
With these snippets you can better understand Python internals.

```python
reversed([]) == reversed([])
# False
wat.s / reversed([])
# value: <list_reverseiterator object at 0x76749d1cb400>
# type: list_reverseiterator
```

```python
wat / type('ObjectCreator', (), {})
# value: <class '__main__.ObjectCreator'>
# type: type
# signature: class ObjectCreator()

wat / type
# value: <class 'type'>
# type: type
# signature: class type(…)
# """
# type(object) -> the object's type
# type(name, bases, dict, **kwds) -> a new type
# """
# 
# Public attributes:
#   def mro(self, /) # Return a type's method resolution order.
```

```python
from typing import List
wat.s / List[str]
# value: typing.List[str]
# type: typing._GenericAlias
# parents: typing._BaseGenericAlias, typing._Final
# signature: def List(*args, **kwargs)

wat(str | None)
# value: str | None
# type: types.UnionType
```

Explore Python built-ins:
```python
wat / __builtins__
wat / ...
```

### Inspect WAT itself
```python
wat.dunder / wat
wat.code / wat.__truediv__
```

## Environment variables
- `WAT_COLOR="false"` to disable colorful output in the console.
- `WAT_COLOR="true"` to enforce colorful outputs even in non-tty environment.

### Color theme
You can customize the color theme by setting the environment variable `WAT_COLORS`.
Here's the default theme which you can modify with your own ANSI color codes:
```sh
export WAT_COLORS="BAR=0;34,TRAIT=1;34,HEAD=1;37,STR=0;32,NUMBER=0;31,NONE=0;35,TRUE=1;32,FALSE=1;31,DOCS=2;37,KEYWORD=0;34,CALLABLE=1;32,SIGNATURE=0;32,VARIABLE=1;33,CODE=0;33"
```

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
