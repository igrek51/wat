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

### Fun Fact: Load from Unicode Glyph
You can load WAT from a single Unicode glyph.
```python
import zlib; exec(zlib.decompress(bytes(ord(c)&255 for c in '🙀󠅸󠆜󠇕󠅜󠇫󠅮󠇛󠅆󠄖ⷾ󠆟󠆧󠄠󠆼󠄿󠅈󠄦󠆪󠆚󠆴󠅻󠄁󠇜󠄲󠄋󠄧󠅕󠅷󠆃󠅵󠇣󠇂󠅶󠅛󠄔󠆶󠅁󠇐󠇢󠇈󠅦󠅍󠆑󠅚󠆒󠆊󠇣󠄕󠄄ⷴ󠄡ⷶ󠄙ⷺ󠅠󠅽󠆒󠄽󠆗󠆹󠆓󠆔󠆕󠆦󠇀󠇮󠄆󠆰󠅄󠇎󠇌ⷹ󠇦󠇌󠆙󠄳󠇧󠄲󠄳󠅊󠆱󠅜󠇕󠅍󠄗󠄔󠅕󠆻󠄒ⷳ󠇮󠅉󠇁󠆯󠅵󠆫󠆞󠄚󠆡󠆞󠇚󠆇ⷶ󠇉󠆼󠇌󠇚󠄶󠅸󠇃󠆍󠅟󠇗󠇕󠆢󠆸󠄹󠅼󠄒󠇀󠆿󠅜󠄬󠆂󠄴󠄭󠆪󠆢󠅋󠇓󠆨󠄕󠇥󠅢󠄒󠆴󠆷󠅀󠄵󠄉ⷲ󠅵󠆕󠆋󠅦󠄒󠅔󠅵󠅞󠇏󠇛󠅉󠅐󠇖󠇕󠇍󠄤󠆘󠇗󠆹󠆀󠇏󠆬󠄬󠆱󠅮󠇕󠄔󠇯󠆲󠅎󠇄󠆌󠆅﻿󠄐󠅢󠅊󠄈󠄉󠅽󠆺󠄕󠆌󠆙ⷰ󠆗󠅛󠇅󠇝󠄤ⷼ󠇥󠅖󠅡󠇏󠄉󠅾󠆸󠇅󠇈󠅊󠆂󠄟󠅞󠄱ⷱ󠆖ⷰ󠆗󠅛󠄥󠇙󠅍󠇤󠆷󠄫󠆕󠆣󠆮󠅫󠆊󠇫󠅵󠄧󠅆󠄅󠅓󠅥󠅋󠄘ⷻ󠆻󠆬󠅜󠇃󠅗ⷷ󠆰󠆒󠆂󠇈󠆮󠅋󠅡󠇄󠄥󠆱󠅁󠆌󠇅󠅍󠆕󠅵󠇫󠄆󠇫󠇪󠆹󠄯󠄢󠇄󠅊ⷰ󠇃󠄭󠄦ⷰ󠆄󠄾󠇝󠄊󠇬󠄮󠇁󠆏ⷾ󠅠󠆱﻿󠅄󠄽󠇬󠄭󠅯󠅟󠄖󠇮󠄄󠄪󠇞󠄓ⷽ󠇤󠄁󠇗ⷳ󠄄ⷾ󠆞󠆠󠆔󠆤󠄊󠆦󠆋󠆺󠅙󠅦󠅝󠅔󠅟﻿󠄴󠄉󠆞󠅊󠄵󠅊󠆾󠇎󠇊󠅖󠅋󠅇󠆽󠇉󠆹󠆖󠅯󠄴󠆽ⷲ󠆙󠇦󠅔󠄽ⷳ󠅄󠇊󠆷󠇕ⷺ󠆺󠄬󠇦󠇪󠄍󠆪ⷸ󠅑󠇊󠅵󠅎󠄪󠆝󠄸󠄊󠄞󠅙󠅪󠆨󠄹󠇠󠆯󠆠󠅮󠄐󠅂󠅳󠅢󠇫󠄸󠅩󠆚󠅮󠆠󠆕󠇌󠆔󠇘ⷺ󠆥󠅋󠆕󠄸󠆫󠆺󠆓󠆬󠇆󠇄󠅘󠆽󠇮󠅖󠇫󠄮󠄩󠆋󠆶󠆋󠇒󠆇󠅂󠆔󠅹󠆪󠇤󠅕󠄖󠆕󠅨󠅙󠅜󠇌󠅾󠇌󠄤󠇅󠄂󠆗󠇬󠆴󠇭󠅲󠄠󠆞󠄖󠅭󠇖󠅵󠄏󠆑󠆥󠄿󠆝󠅨󠆖󠅅󠆕󠆕󠇩󠅽󠆑󠅷󠆷󠅉󠇝󠅎󠅯󠅄󠆗󠇪󠇒󠆶ⷸ󠆗󠆈󠅢󠅘󠄝󠇥󠅺󠅙󠆙󠆕󠇄󠆌󠅌󠆡󠅳󠇑󠅴󠇑󠅳󠆘󠆟󠇮󠆡󠄔󠇓󠅗󠅇󠆧󠇁󠆳󠄠ⷼⷵ󠇟󠄿󠆇󠇁󠅓󠄏󠄚󠄪󠅎󠅧󠅧󠆳ⷳ󠇘󠄇󠇉󠅖󠄫󠅑󠇥󠇑󠆇󠄢󠄴󠄂󠄔󠆩󠄊󠇂󠇋󠄪󠆜ⷾ󠅔󠄗󠅕󠇄󠅰󠄱󠅩󠇑󠆣󠇂󠄹󠅔󠇂󠇡󠅷󠆹󠇎󠆍󠅘󠆈󠄾󠅘󠄴ⷵ󠄲󠅈󠅯󠅄󠄥󠄚󠆘󠆎󠆔󠄛󠄁󠇪󠆢󠆎󠆘󠆉󠆶󠅫󠅒󠅞󠅥󠅒󠅡ⷹ󠆍󠆻󠆢ⷹ󠄿󠅯󠇖󠅂󠄱󠆼󠅒󠆍ⷱ󠄑󠇛󠇨󠄩󠄲󠅵󠅁󠆒󠄠󠄪󠇕󠆢󠄾󠆸󠄵󠄩󠅔󠄕󠆫󠄔󠆦󠆣󠅮󠄢󠇝󠅹󠇜󠇣󠄻󠇜󠆰󠄸󠇏󠅏󠆏󠇞󠆜󠅯󠆩󠇑󠇡󠆆󠆄󠆷󠄍󠄶󠆚󠅮󠄛󠄒󠆝󠄀󠇍󠅿󠄄󠄁󠅈󠇆󠇩󠅇󠆩󠆐󠅷󠆛󠄌󠅫ⷾ󠄾󠄻ⷺ󠅪󠆻󠄱󠆣󠇚󠇊ⷺ󠅐󠇋󠆓󠆌󠆓󠄒󠄧󠆾󠅄ⷴ󠆁󠄂󠅡󠅹󠄍ⷶ󠆅󠅭󠅜󠄖󠆱󠅄󠇂󠆮󠆲󠅆󠅔󠅝󠆛󠆄󠆓󠅀󠄪󠅋󠆊󠅚󠇎󠇅󠇔󠆰󠆵󠄺󠇑󠆳󠄢󠇉󠄞󠆑󠆍󠅪󠆥󠄻󠆗󠄅󠆲󠅯󠇔󠄱󠅩󠅎󠄣󠇨󠄔󠇖󠅟󠇃󠇪󠄑󠆦󠅩󠄩󠆪󠄴󠄅󠆦󠇞󠇖󠆕󠆈󠇭󠅅󠇙󠄼󠆘󠆗󠇑󠆎󠆁󠇚󠅴󠇪󠇪󠄟󠅔ⷱ󠅘󠆬󠄩󠄒󠇯󠇧󠅢󠇕󠄅󠇧󠄰󠇎󠅙󠇓󠇔󠆍󠇛󠇃󠄊󠆜󠅗󠆏󠅟󠆄󠄰󠇍󠇈󠇋ⷸ󠅃󠇀󠅂󠄚󠅃ⷸ󠇫󠇏󠆿󠆄󠅦󠅱󠄛󠆣󠅏󠆢󠅖󠆐󠆩󠄮󠆏󠇘󠄁󠇪󠅕󠄰󠆮󠅻󠆊󠇂󠆚󠅞󠅕󠄤󠆇󠆇󠄎󠆄󠆺󠆁󠆇󠇁󠆵󠄇󠆃󠆂󠆪󠄠󠆫ⷲ󠄠󠅂󠆣󠄪󠅗󠄽󠅛󠇪󠆘󠇊󠅇󠄆󠇍󠆔󠅠󠄀󠇗󠅕󠄗󠆡󠆱󠆉󠅱󠄝󠄾󠇟󠄹󠄽󠅟󠆝󠆼󠄾󠇛󠄞󠄜󠄜󠅬󠆀󠆒󠆾󠅭󠄕󠇯󠆯󠄸󠄋󠄁󠇭󠇍󠅅󠄏󠄧󠄤󠆧󠄿󠆁󠄎󠄬󠆰󠄫󠇟󠆂󠆡󠅛󠆡󠄁󠅊󠆫󠄇󠇆󠆞󠅂󠄒󠅭󠅊󠆜󠄑󠇚󠄡󠅄󠆽󠅮󠇦󠅲󠆞ⷸ󠄹󠅅󠆰󠇈󠆙󠄚ⷴ󠄣󠅔󠆷󠆇󠅢󠅲󠅃ⷲ󠅶󠅪󠇎󠄮󠆫󠄍󠆗󠆚󠅕󠅡󠇍󠄃󠅹󠅕󠄃󠆜󠆩󠇠󠆩󠅍󠅚󠆨󠄐󠅹󠆔󠄖󠇠󠄊󠅒󠅓󠇮󠇘ⷲ󠅉󠅰󠄧󠄞󠆒󠄲󠅛󠅞󠇧󠄙󠇑󠄞󠇒󠄧󠅅󠅅󠄽󠇝󠄢󠆋󠄎󠇫󠄳󠆗󠅸󠅭󠇚󠆂󠆬󠆊󠆺󠅪󠄣󠄃󠆯󠆡󠇙󠆙󠇬󠇪󠆜󠆹󠆆󠇅󠆇󠅌󠅀ⷴ󠄒󠇤󠅅󠇣󠆩󠆐󠄌󠄖󠆠󠄞󠇜󠅰󠇖󠅴󠇭󠅽󠇑󠇝󠅆󠆰󠅶󠅂󠇖󠄼󠆬󠄀󠆆󠆬󠅢󠅇ⷻ󠄸󠇆ⷰ󠅕󠆗󠆋󠅣󠅷󠄶󠆠󠆮󠄫󠄪󠄫󠇚󠅓󠆁󠅄󠆯󠅯󠇙󠄵󠄡󠅊󠆨󠅱󠇫󠇃󠅎󠇋󠅙ⷹ󠄀󠄘ⷻ󠆖󠇥󠅕󠇖󠆊󠄙󠄽󠆂󠄸󠆃󠆬󠄍󠇄󠄐󠆌󠅡󠄮󠇭󠇅󠆛󠄑󠆻󠆳󠄏󠄰󠄢󠇀󠆇󠄌󠆢󠅣󠄔󠆖󠅮󠅂󠅋󠆌󠇬󠆪󠆙󠄆󠇛󠅈󠇈󠆸󠆛󠇌󠆄󠆔󠄨󠄾󠄿󠄊󠇂󠅚󠇤󠄇ⷹ󠅤󠇋󠄒󠇃󠅋󠅢󠆅ⷵ󠄔󠅧󠇋󠆁󠆙󠄐󠄿󠅉ⷽ󠅠󠄿ⷱ󠅢ⷾ󠆤󠄟ⷻ󠄧󠅮󠄖󠆀󠄱󠆳󠇔󠇐󠅇󠅍󠄬󠇏󠆄󠄳󠆳󠆩󠄥󠅝󠇩󠄼󠄌󠆥󠆲󠄡󠆦󠇄ⷸ󠅟󠄹󠇝󠇑ⷷ󠄸󠄦󠅲󠄥󠄓󠇣󠅕󠇢󠇁󠄎󠇀󠅀󠆰󠄝󠆈󠆤󠆡󠅸󠅽ⷲ󠇕󠅬󠄋󠄞󠅃󠄖󠇇󠇚󠄪󠄌󠄙󠆯󠅃󠅋󠆟󠇅󠆢󠅸󠆟󠆄󠆜󠅫󠆩ⷰ󠇅󠄥󠆫󠄛󠆈󠄄󠄡󠇠󠅛󠆬󠄫󠅚󠇘󠄣󠄐󠅙ⷻ󠅐󠇍󠄩󠄱󠄛󠆄󠅱󠆨󠇑󠅺󠆚󠆪󠆥󠇨󠅮󠇫󠅼󠆠󠇢󠅺󠅝󠆔󠅝󠅡󠅈󠅮󠆳󠅶󠇈󠅗󠄎󠄰󠅣󠆳󠅡󠆻󠄆󠅕󠄟󠇚󠄡󠆯󠆶󠆶﻿󠆘ⷽⷸ󠇃󠇉󠄩󠆄󠅓󠇜󠅬󠆫󠅤󠅻󠅴󠅼󠅼ⷴ󠇪󠅸󠆶󠇝󠅠󠆇󠄪󠇀󠇚󠆘󠇩󠄰󠄱󠄗󠄩󠅏󠅯ⷲ󠅛󠅭󠇗󠅖󠅨󠄲󠆒󠆋󠄫󠇙󠄽󠅙󠇍󠅕󠇝󠆦󠅵󠅕󠄾󠆀󠇡󠆄󠇪󠆬󠆫󠅥󠅖󠅥󠆷󠆹󠆻ⷷ󠆛󠆠󠄯󠇖󠆦󠄒󠄋󠆗󠅨󠄬󠆡󠆧󠄩󠆽󠄈󠄰󠆱󠄭󠄧󠆬󠅭󠇤󠆺󠅟󠆪󠆟󠇞󠄕󠅠󠆮󠇀ⷳ󠄪󠅩󠅿󠆫󠆨󠆦󠇟󠆞󠆜󠆽󠄹󠅿󠅳ⷲⷶ󠇨󠄸󠄽󠅹󠅻ⷼ󠆣󠅫󠅳󠇆󠅹󠇖󠄌󠇩󠇉󠄟󠅭󠇫󠅇󠅊󠄠󠄓󠆕󠆵󠇨󠆹󠄠󠆅ⷾ󠇔󠄲󠇝ⷻ󠅊󠅬󠇏󠅑󠅾󠅿󠅴󠆚󠆚󠆑󠄎󠄎󠆲󠄯󠅴󠆷󠄗󠄚󠇤󠅣ⷽ󠅈󠆝󠄢󠅑󠆒󠆋󠄘󠄃󠇟󠅛󠄨󠅏󠆇󠆅ⷲ󠄘󠆷󠄎󠅢󠅏󠅇󠅓󠆭󠄵󠄑󠄽󠇅󠅖󠄪ⷵ󠇨󠄬󠇮󠄱󠆃󠅙󠅳󠇓󠅢󠆲󠆕󠆸󠇕󠄺󠅿󠄠󠆈󠇘󠅒󠅹󠆑󠇛󠅆󠅎󠆑󠅯󠅻ⷶ󠄍󠄵󠆞󠇗󠅱󠆚󠅕󠇠󠅽󠄳󠅲󠆖󠅅󠅋󠇡󠆐󠆚󠆎󠄳󠄵󠇌󠆩󠅘󠆮󠄺󠇋󠅦󠆫󠆾󠆂󠅧󠅉󠇠󠅲󠄖󠅼ⷲ󠇒󠄤󠄁󠄆󠄹󠄚󠇬󠅏󠆥󠄅󠇒󠆠󠄨󠇔󠅡󠅳󠇐󠄓ⷵ󠆀󠅩ⷸ󠄈󠄅󠇞󠅃󠅳ⷶ󠅒󠅜󠇄󠆗󠇊󠆻󠄟󠆸󠅂󠄟󠅮󠄃󠅰󠅯󠇘󠆈󠅲󠇇󠅤󠅊󠇃󠇘󠄝󠇭ⷸ󠄌󠄚󠆾󠆼󠄙󠇜󠇁󠇑󠇡󠇠󠄄ⷺ󠄽󠇅󠄽󠄮󠅠󠇖󠆲󠅵󠇙󠇭󠇍󠆂ⷸ󠇧󠄚󠅖󠅚󠆐󠄄󠅡󠄒󠆎󠆍󠅥󠄄󠆄󠄣󠆢󠄐󠅩ⷷ󠄙󠇑󠆆󠆻󠇚󠅺󠇙󠆩󠇃󠆶󠄞󠆏󠇚󠇐󠅱󠅗󠆘󠆭󠆒󠆖󠅔󠄬󠅹󠇨󠆭󠄜󠄕󠆠󠆚󠄺ⷲ󠆺󠇋󠄺󠅟󠆗󠇂󠇤󠇙󠆨󠄾󠄡󠄄󠅥󠅅󠅵󠄓󠅚󠅁󠆺󠆠󠅝󠆘󠄲󠆂󠆎󠇦󠆷󠅞󠅜󠄍󠇠󠅔󠄼󠆽󠆁󠇘󠅢󠄕󠇅󠅎󠄬󠇍󠅐󠇓󠇐󠆣󠆱󠆆󠇤󠇐󠅞󠅠󠅮󠅮󠄑󠅝󠄽󠅹󠆌󠇂󠅍󠇀󠇁󠄨󠆴󠇫󠇫󠄨󠆼󠆸󠆼󠆼󠆿󠆼󠆜󠅞󠄽󠆃󠅱󠄡󠇣ⷴ󠅩󠄏󠄾󠆶󠄖󠇏󠆈󠅨󠅴ⷲ󠅎󠆂󠆱󠇍󠄌󠅱󠇡󠅬󠇂󠅘󠇀󠄃󠆁󠆊󠅤󠇍󠅥󠅠󠄰󠅨󠅡󠇅󠇠󠇥󠅤󠆂󠅗󠄿󠇯󠄜󠆈󠅗󠄥󠆐󠇒󠅌󠆠󠅢󠄢󠆓󠆧󠆪󠇀ⷴ󠇤󠇌󠆏󠅊󠄧󠄐󠆲󠇧󠆢󠅢󠆾󠄸󠅎ⷵ󠄒󠄔󠇍󠇦󠄢󠄫󠅊󠄰󠆰󠅝󠆍󠅂󠄋󠇬󠅔󠄶󠇘󠆐󠄠󠅄󠆌󠄫󠇕󠇡󠇞󠇙󠅶󠆐󠆼󠅣󠆀󠅮ⷱ󠄪󠆛󠄸󠇛󠄑󠆰󠇎󠅐ⷰ󠄽󠄦󠅴󠇆󠄡󠆃ⷼ󠄩󠇭ⷺ󠅅󠆎󠄼󠆉󠅾󠅁󠄝ⷲ󠆢󠅌󠄩󠆉󠄖󠄕󠅭󠄑󠅖󠄷󠆑󠅉󠄎󠆬󠅬󠄗󠄖󠅠󠅓󠅐󠆦󠆅󠅯󠅞󠄒󠅋󠆋󠆓󠆜󠆞󠆻󠅜󠄩󠆙󠄞󠅋󠆘󠄆󠆲󠅹󠄬󠄷󠅣󠆲󠅐󠄽󠄎󠅵󠄍󠆃󠆠󠅰󠆝󠇞󠅙󠇭󠆰󠅳󠅼ⷲ󠆴󠄩󠄈󠅺󠆆󠅚󠄧ⷽ󠅛󠇏󠆪󠄪󠇤󠄭󠇘󠆭󠆍󠇮󠅕󠅍󠆠󠇇󠅕󠄧󠇞󠅷󠄪󠆫󠄯󠆚󠆖󠄷󠆏󠄧󠅁󠆊󠇫󠆫󠇭󠄒󠆬󠇆󠆐󠆵󠄫󠇈󠄎󠇑󠆎󠆐󠄉󠄽󠇚󠄎󠇣󠅾󠅜󠇡󠇎󠅎󠆭󠄁󠆊󠇣󠇠󠅥ⷰ󠇢ⷹⷳ󠆾󠇢󠇩󠄦󠄗󠆇󠅐󠅿󠆥󠄶󠆻󠅩󠄷ⷼ󠇧󠅟󠇜󠄄󠅀󠆷󠇭󠅏󠆰󠅌󠅎󠄆󠆦󠅗󠅎󠄒󠅉󠇉󠇬󠆩ⷵ󠄗󠄀󠅈󠇖󠅈󠄲󠆂󠆾󠅍ⷰ󠅂󠇥󠄻󠄶󠇒󠆜󠆸󠅝󠄵󠅾󠅤󠇯󠆬󠇗󠆯󠅉󠅓󠄂󠅻󠄟󠇬󠄏󠆲󠄚ⷷ󠇔ⷶ󠇘󠅐󠇛󠄁󠅻󠆈󠆛󠅑󠇎󠄆󠄛󠄔󠅨󠇬󠇋󠇊󠇟󠆱󠅳󠇁󠅷󠄀󠆻ⷹ󠄔󠄯󠄞󠅻󠇝󠅠󠇊󠄱󠄁󠄃󠆆󠆖󠄨󠅹󠅮󠆦󠆥󠅨󠇁󠅐󠅴󠅙󠄵󠇗󠇍󠅱󠅑ⷴ󠆻󠄼󠆐󠅬󠆟󠆝󠆟󠅮󠇃󠆍󠇜󠆂󠆗󠆬󠄞󠄨󠄰󠄾󠄫󠄘󠄳󠄭󠇚󠄌󠆿󠄽󠅹󠄻󠇛󠅢󠄓󠅧󠆨󠄶󠄽󠅲󠄻󠅎󠅿󠅾ⷺ󠇝󠅬󠆋󠅍󠅆󠇩󠄩󠆜󠄟󠄇ⷸⷺ󠇨ⷸ󠅬󠆶󠆥󠅆󠄾󠅄󠅟󠄞󠅑󠅑󠅵󠆓󠅠󠅑󠇖󠅙󠄗󠄏󠄈󠅆󠄏󠇪󠆻󠅯󠅞󠇍󠅎󠆷󠆛󠆁󠆓󠆅󠅁󠇘󠆼󠆘󠅷󠇣󠅮󠄏󠅫ⷻ󠆳󠆨󠄦󠄐󠄖󠇦󠆋󠅸󠄜󠄚󠇏󠇨󠇆󠆡󠆱󠅶󠄟󠅨󠅹󠇔󠆒󠇠󠆉󠆐󠆵󠄷󠆖󠅕󠄷󠄐󠇑󠅜󠄷󠇙ⷼ󠄎󠆼󠄏󠄅󠄋󠄘󠄗󠄬󠇖󠅥󠅉󠄯󠅑ⷸ󠅥󠄴󠅽󠄚󠆿󠄌󠄧󠄊󠅁󠅳󠄺󠅀󠄺󠄮󠅏󠄲󠆠󠅟ⷶ󠄍󠅭󠄟󠅃󠇆󠄪󠄯󠅢󠇇ⷶ󠆾󠅴󠆦󠇀󠅇󠅇󠄵󠅖󠆇󠅉󠇃󠅛󠄒󠇖󠄌󠇀󠆣󠄫󠄤󠅫ⷹ󠆰󠇐󠅞󠄆󠆟󠄏󠆘󠅕󠅗󠇝󠅦󠆧󠆧󠄧󠆧󠆇󠇠󠇜󠅫󠄈ⷸ󠄠󠅨󠅺󠄈󠄪󠆰󠇙󠄢ⷷ󠅕󠄅󠅍󠄛󠅚󠅱󠇨󠅵󠆇󠆺󠅱󠄨󠆳󠇙󠅺󠆚󠇖󠆉󠅥󠆛󠅠󠄤󠇬󠅚󠆂󠄻󠆏󠅿󠄻󠇞󠆗󠆪󠇠󠆷󠄈󠅹󠅣󠅹󠄒󠆼󠇣󠆝󠇥ⷹ󠆔󠇀󠆣󠇘󠅱󠆻󠆮󠆿󠆥󠄖󠇤󠅇󠇍󠅩󠄗󠆕󠇅󠆏󠆍󠅃󠅭󠄔󠅩󠄄󠅧󠄮󠆽󠅑󠇒󠆑󠅪󠅢󠅎󠅟󠆣󠄐󠅋ⷱ󠇐󠅖󠇫󠄰󠇠󠄗󠇝󠅶󠇂󠆃󠄨󠄰󠄱󠅡󠇦󠅔󠅠󠅚󠇡󠄁󠄭󠇙󠅂󠅍󠄛󠅉󠇢󠅏󠇔󠄂󠇘󠇍󠄪󠇘󠅭󠇢󠄃󠄟󠄌󠇜󠄘󠇛󠆶󠅦󠅙󠄋󠆰󠅬󠆻﻿󠆂󠅦󠆕󠅃󠇦󠇁󠄝󠇦󠇅󠇕󠆐󠅞ⷵ󠇜󠆋󠇇󠄼󠅉󠄛󠆊󠅑󠇜󠇘󠇉󠇯󠆯󠄩󠄗󠆻󠄕󠇥󠇪󠅿󠅆󠅏󠄮ⷶ󠅗󠆓󠆫󠅁󠄭󠇑󠆧󠇏󠆩󠆜󠄫󠇎󠄥󠅩󠅋󠄿󠆝󠆚󠇔󠅒󠇉󠆘󠇟󠆕ⷳ󠇅󠅐󠅐󠆖ⷰ󠆡󠄾󠅐󠇐󠇆󠅵󠅪󠇓󠄾󠅦󠅞󠅔󠅟󠆜󠆫󠅭󠅷󠅚󠅔󠆦󠅠󠇤󠇭󠅴󠆔󠅔󠇧󠄭󠆽󠄃ⷰ󠇔󠇨󠆾󠇚󠆼󠆦󠅢󠅎󠆤󠆛󠇚󠇝󠆽󠆦ⷹ󠄂󠅙󠆾󠆟󠄄󠇗󠅙󠄫󠄈󠄇󠅧󠅏󠅔󠇫󠄥󠇝󠆘󠆈󠆴󠆠󠆐󠆴󠆟󠅔󠄓󠄱󠇅󠆄󠄨󠄫󠄋󠆣󠇅󠅃󠄋󠇈󠆜ⷺ󠄩󠅵󠇯󠆈󠄋﻿ⷱ󠆩󠆌󠄳󠅫󠄚󠅌󠆟󠆐󠄌󠅝󠇢󠆐󠅱󠄾󠇮󠅱󠄤󠆪󠄆ⷼⷸⷼ󠄮󠆥󠆲󠇨󠇏󠅺ⷹ󠇐󠆻󠄵󠅴󠅼󠅅󠄌󠄻󠇇󠇓󠆅󠄑󠄽󠄹󠇇󠅸󠆺󠅮󠆺󠆀ⷼ󠆲󠅲󠇀󠇌󠄐󠆼󠆃󠅔󠅹󠄭󠄈󠄩󠄎󠄃󠅧󠆎ⷻ󠅰󠇛󠅃󠆫󠄐󠇕󠆽󠆪ⷻ󠅱󠆲󠇃󠄈󠄦󠆵󠄩󠇊󠄓󠅒󠄚﻿󠄜󠄱󠄗󠇖󠆚󠄝󠄦󠆉󠆝󠆴󠅴󠆟󠅱󠆈ⷷ󠄫󠅈󠆑󠅚󠇈󠆛󠇌󠅑󠄾󠄢󠄪󠆕󠄜󠄿󠆖󠅭󠆽󠅜󠆆󠄯󠅅󠅱󠇋󠇤󠄢󠄣󠅍󠇌󠅐ⷵ󠆨󠅄󠆧󠄺󠇪󠅞󠆚󠇉󠅗󠄲󠅵󠅰󠇊󠇛󠄮󠆲󠅾󠄗󠆐󠄆󠅡󠄊󠄦󠇟󠅍󠇀󠅭󠇌󠇎󠆨󠇅󠇬ⷰ󠄍󠆣󠆡󠆁󠅇󠇡󠆷󠅄󠅧󠆝󠆆󠆇󠄓󠄇󠇋󠆜󠅒󠇋󠆎󠅤󠄲󠅦󠄏󠇚󠄙󠇠󠄇󠅵󠆮󠅀󠆜󠇞󠅭󠆴󠆱󠇮󠆭󠄃󠅫󠅛󠅘󠄟󠇒ⷹ󠅗󠄒󠇂󠇮󠇛󠇆ⷲ󠇎󠇧󠄇󠅁󠄠󠅁󠇇󠇃󠇕󠄡󠇭󠅑󠄻󠄡󠄻󠅕󠅇󠄝󠆧󠅞󠄙󠄒󠇎󠆭󠅇󠆧󠇝󠆥󠇠󠅑󠇊󠆓󠄻󠅯󠅕ⷰ󠄥󠄨󠇢󠅰󠅻󠇨󠄬󠅒󠇂󠄅󠅈󠄅󠅍󠅬ⷺ󠆢󠇛󠅣󠅇󠇇󠇎󠇘󠄉󠆃󠇦󠇃󠄞󠆅󠄏󠄚󠆎󠄰󠄰󠇒ⷼ󠇑󠅍󠄇󠆞󠆚󠄁󠆛󠆚󠆋󠅕󠅷󠇫󠅘󠅞󠅥󠅂󠇧󠇫󠄆ⷽ󠄑󠄷󠆋󠄵󠄻󠄩ⷲ󠇒󠅀󠇒󠇡󠇒󠇚ⷶ󠅌󠇭󠅽󠆻󠄹󠆯󠇩󠆁󠄾󠆧󠆋ⷴ󠄚󠇘󠅰󠄼󠄧󠆖󠄻󠅊󠆤󠇄󠇙󠅆ⷺ󠅩󠄒󠅈󠅝󠆲󠅶ⷷ󠄾󠅨󠅂󠄫󠇢󠆰󠄊󠇤󠅥󠄖󠄍󠄼󠆽󠄓󠄏󠄘󠇌󠄏󠅮󠆖󠅹󠅡󠆞󠄤󠆹󠅀󠆬󠄫󠇉󠆊󠄦󠄛󠇞󠄺󠆓󠄗󠄏󠄜󠇊󠆸󠅿󠇙󠅪󠅠󠄧󠇭󠄷󠅬󠆢󠅙󠆻󠅝󠇖󠄎󠆚󠄾󠅠󠇢󠄽󠇫󠇋󠇋ⷷ󠄯󠆮󠄯󠄯󠄯󠄮󠄯ⷳ󠅧󠇑󠄗ⷸ󠄙﻿󠅵󠆉󠇁󠄧ⷼ󠄑󠆕󠆼󠅄ⷽ󠅃󠄦󠄝󠇒󠇁󠇁󠆁󠆼󠅫󠇁󠄇󠇭󠆔󠅢󠇣󠇞󠆬󠅸󠆟󠄭󠇁󠇇󠄅󠇫󠇪󠆮󠆪󠇯󠄫󠄙󠄮󠆴󠇐󠆞󠆭󠅴﻿󠆾ⷵ󠇓󠆧󠇪󠄶󠇨󠇝󠄽󠄞󠇏ⷹ󠅷󠆨󠅓󠆷󠄺󠅱󠅟󠆽󠆶ⷲ󠆆ⷰ󠅦󠄻󠆂󠅑󠅔󠇩󠆪󠆩󠅯󠇐󠇛󠅙󠇇󠆚󠇌󠄕󠇝󠅽󠅤󠆮󠅜󠅍󠅆󠄅󠆾󠇏󠆺󠅁󠄔󠅗󠆩󠆹󠄳󠆰󠇆󠄐󠆼󠇝󠆊󠇒ⷶ󠇁ⷺ󠄔󠇅󠇪󠄑󠅳󠇬󠅞󠆇󠆪󠇡󠆗󠄿󠄜󠆝󠄇󠅆󠇈󠄬󠇈󠆗󠄖󠆹󠇕󠆍󠄇󠆁󠅓󠆖󠄬󠇂ⷳ󠇦󠇁󠄉󠅎󠅠󠄌󠇁󠆧󠄒󠅈ⷹ󠅹󠅀ⷶ󠆚󠅌󠄡󠅌󠄭󠄖󠆅󠄀󠇓󠇤󠄷󠆆ⷹ󠆕󠄢󠄀󠆫󠇥󠇐󠄹󠇭󠆦󠇎󠆝󠇒󠅯󠄔󠆜󠅂󠆁󠇘ⷶⷰ󠆲󠇒󠇚󠆍󠆻󠄍󠅼󠇑󠆬󠇏󠄓󠇗󠅙󠇝󠇟󠄖󠆹󠇭ⷺ󠄂󠆳󠆌󠇈󠆎󠅊󠆛󠄘ⷻⷰ󠇬󠆣󠄬󠄜󠆒󠆝󠆾󠇂󠆥ⷱ󠅼󠄺󠅜󠇍󠄽󠆪󠆪󠆮󠄾󠇉󠆮󠆯󠄛ⷱ󠆮󠄀󠆟󠆛󠆳󠅭󠇠ⷾⷳ󠅺󠄎󠄑󠆶󠄼󠇎ⷰ󠇁󠄰󠆢󠇪󠆁󠅙󠇧󠄘󠅁󠄍󠅮󠄡󠅐ⷷ󠅛󠄦󠅲󠄰󠅴󠅁󠄐󠄗󠆟󠄏󠇇󠅛󠆻󠆾󠅬󠄜󠄎󠇈󠇈󠄩󠅀󠇦󠆐󠆠ⷺ󠄃󠅥󠅷󠅠󠆁󠇁󠆄󠇜󠄇ⷸ󠆇󠅄ⷷ󠆷󠆢󠆁󠇕󠅽󠄫󠇔ⷴ󠄣ⷶ󠅽󠇖ⷲ󠄭ⷹ󠇜󠄇󠇣󠅘󠇈󠄇󠇃󠅃󠅿󠄙󠄦󠇭󠆐󠄸󠄀󠄺󠇚󠄶󠄯󠇗󠄸󠇣󠄥󠆦󠇍󠅬󠅃󠄇󠄤󠄋󠅋󠇆󠄢󠆒󠄋󠇈󠅢󠄗󠄦󠅩󠅔󠅙󠅻󠆚󠇘󠄵󠇃󠅘󠅼󠆍󠄽󠇠󠇓󠄈󠆲󠅹󠄢󠇋󠅱󠇎󠅨󠄢󠆡󠇌󠅇󠆺󠅩󠆲󠄇󠄋󠄪󠄯󠅚󠆺󠆻󠅆󠆶󠅸󠆱󠄮󠄕󠅠󠇁ⷰ󠅠󠆹󠇚󠆺󠄔󠅽󠆥󠆁󠇖󠄖󠆊󠅀󠄩󠇌󠅻󠄨󠅭󠄏󠇦󠄵󠇊󠇌󠅟󠇚󠅥󠄍󠄳󠇖󠆎󠆯ⷽ󠄨󠄞󠅘󠇪󠅄󠄔󠄘󠇧󠄸󠆂󠅽󠅓󠇖󠇗󠄖󠆸󠄅󠇀󠄵󠄖󠅂󠇨󠅛󠅗󠅥󠆼󠅡󠅌󠄩󠄤󠅍󠇐󠄨󠆏󠆼󠆬󠆔󠅬󠅚󠇟󠆝󠇩󠄶󠄴󠄋󠅖󠄙󠅛󠅘󠅔󠅐󠇣󠅩󠇐󠅡󠆠󠇃󠇩󠄹󠄚󠄌󠇈󠆠󠅤ⷰ󠆤󠅂ⷾ󠄊󠅩ⷵ󠄐󠅩󠇂󠆩󠄜󠅙󠅄󠆈󠇖󠅽󠅋󠄼󠇒󠇥󠄶ⷻ󠅂󠇭󠄸󠄩󠄙󠇏󠅾󠄿󠅳󠅓󠄻󠆚󠄠󠆎󠆛󠅕󠄼󠇅󠄓󠅭󠇂󠄰󠄺󠆉󠆴󠆼󠆢󠇏󠆔󠅴󠄦󠄦󠇈󠄲󠆘󠄐󠄅󠄜󠆻󠄚󠄐󠄚󠄉󠄫󠅁󠆰󠆀󠅫󠇐󠅀ⷻ󠅼󠅤󠇌󠅩󠆺󠅷󠆼󠅺󠇗󠅚󠇥󠆯󠅩ⷼ󠅟󠄜󠄡󠄸󠇎󠇞󠅐󠅔󠄐󠄏󠄀󠆤󠄼󠇀󠆄󠇛󠇃ⷲ󠅛󠆕󠇙󠅃󠇊󠅵ⷺ󠅇󠄩󠄶󠄙󠅈󠇋󠆡󠄜󠆽󠄷󠇠󠆴ⷲ󠄡󠇬󠅀󠄄󠄷󠄟󠆢󠄐󠇚󠅁󠄜󠅥﻿󠆐󠅩󠄈󠄓󠆇󠄷󠄴󠄿󠇎󠄵󠇗󠄅ⷾ󠇪󠆦ⷴ󠇤󠄵󠄪󠅦󠄷󠇂󠄡󠇅󠅓󠄱󠅗󠅯󠄉󠅔󠇢󠅞󠅅󠅏󠇎󠄈󠆈󠇊󠇈󠇉󠄎󠆛󠄙󠅃󠆶󠇨󠇭󠄡󠆩󠅖󠄛󠄹ⷾ󠄐󠇖󠄮󠅾󠆡󠅙󠇄󠅯󠅚󠇄󠇡󠆶󠄯󠄐󠇃󠄉󠆇󠇆󠆉󠇬󠅧󠅕󠆯󠄢ⷷ󠇪󠄸󠆶ⷴ󠆢󠇃󠄡󠇥ⷰ󠇇󠇐󠄧󠆛󠆮󠅗󠄹󠅮󠆋ⷹ󠇊󠆄󠄭󠅁󠆺󠄉󠇄󠆽󠆰󠅤ⷻ󠅴󠆽󠆖󠄺󠄂󠄵󠆃ⷰ󠄃󠄻󠇙󠇒󠄘󠄩󠅏󠄳󠇥󠅒󠅢ⷽ󠇬󠇅󠆡󠅻󠅘󠅊󠆹󠅼󠄜󠅛󠇩󠆫ⷻ󠆠󠆞ⷲ󠄄󠄍󠇩󠆩󠆣ⷷ󠆞󠇉ⷵ󠆡󠅻󠅷󠄥󠄨󠇝󠅴󠄘󠇮󠆇󠇘󠅽󠅦󠅘󠄽󠅶󠆲󠇣󠅘󠆑󠅁󠄐󠆩󠅫󠄻󠄰󠆼󠆛󠆘󠇕󠄻󠅦󠄵󠇙󠆄󠄋󠆬󠄉󠄏󠄃ⷹ󠅛󠇄󠆰󠆃󠇞󠇠󠄕󠄻󠇝󠄒󠅺󠇝󠅎󠆡󠅽󠇑󠇔󠄕󠅷󠄆ⷱ󠅺ⷺⷺ󠇤ⷸ󠇤󠆔󠄒󠆧󠄘󠆜󠇭󠆽󠅨󠆢󠇘󠄑󠆺󠇮󠅠󠄼󠄱󠆖󠆌󠇩󠆖󠆾󠅠󠄇󠅾󠄵󠇨󠇧󠄄󠇆󠆌󠆳󠄲ⷹ󠄙󠆳󠄥󠄊󠄺﻿󠄞󠅜󠄴󠄴󠄦󠆬󠇖󠄂󠄴󠅄󠅴󠅶󠇀󠆿󠅶󠇜󠄷󠄽󠇯󠄩󠇈󠆠󠅙󠄶󠅻󠆛󠇔󠅇󠅬ⷻ󠅲󠆜󠆀󠆼󠅸󠆧󠇝󠆹󠇯󠅭󠅬󠅜󠇥󠆗󠆸󠆍󠄅󠆒󠇥ⷹ󠇇󠄁󠆔󠇭󠅭󠆱󠇨󠄾󠄎󠆣ⷹ󠄝󠄰󠇪󠇦󠄣󠅹ⷸ󠅘󠆀ⷲ󠄣󠄇󠄠󠆯󠆾󠄹󠆿󠆻ⷶⷼ󠄑󠆚󠅞󠄓󠄳󠄹󠄋󠇉󠅸󠄗󠅊󠄝󠇉󠆿ⷸ󠇎󠅄󠇛󠅤󠅗󠆳󠄯󠄤󠇉󠇕󠇀󠅕󠅳󠄃󠄫󠄵󠄿󠇤󠄜󠆑󠄝󠅖󠄮ⷰ󠆛󠄓󠄯󠄪󠆡󠇐󠄌󠆟󠄸󠆯󠇁󠄧󠄨󠇚󠆗󠄏ⷶ󠅮󠆻󠆘ⷸ󠄀󠇏󠇩󠄹󠆠󠇝󠇠󠅸󠇓󠆒󠅃󠇄ⷰ﻿󠄫󠇦󠇬󠄏󠅃󠆦󠄝󠆿󠅵󠄜󠅌󠇮󠄎󠅄󠅂󠅾󠇄󠅈󠄬󠅔󠄘󠇊󠇟󠆼ⷼ󠅧󠅴󠄬󠄰󠅿󠇡󠅨󠇢󠆰󠄣󠅓󠅨󠆲󠄂󠄘󠇔󠆿󠅺󠆢󠅻󠆔󠅣󠅡󠄇󠅯󠇤󠆝󠅡󠇮󠇆󠄠󠆯󠆎󠅎󠆓󠄐ⷷ﻿󠄮󠆞󠅿ⷱⷹ󠄟󠆗󠆜󠆛󠇑ⷱ󠆐󠄬󠅾󠅡󠆊󠅱󠅃󠇇󠆔ⷾ󠅅󠆖󠅂󠆢󠅪󠄐󠄾󠆓󠆅󠅼󠇥󠇇󠆔󠆿󠅐󠇥󠄧󠅯󠅧󠆦ⷴ󠅏󠆺󠆿󠇯󠅦󠄆󠅘󠅡󠇐󠄉󠆾󠄩󠅖󠄐󠅸󠄻󠅌󠆖󠅾󠅦󠆸󠆐󠅷󠇌ⷻ󠅣󠅑󠄿󠆻󠇩󠇣󠆫󠆍󠅕󠅓ⷳ󠆹󠆢󠆁󠆬󠇖󠄠󠆩󠇒󠇞󠇮󠆥󠅷󠇦󠄺󠆿󠅝󠅗󠅷󠆸󠅲󠄗󠅅󠆉󠇗ⷲ󠆯󠇫󠆺󠄄󠇫󠄸󠄖󠄧󠆜󠇉󠅀󠄁󠄼󠅠󠄁󠇥󠆓󠄰ⷶ󠅢󠄔ⷾ󠆙󠄘﻿󠇧󠄄󠄈󠆭󠄎ⷶ󠄔󠅅󠇢ⷽ󠆂󠆣󠆕󠆷󠆉󠆍󠅁󠆅󠇀󠅶󠆅󠅁󠄈ⷾ󠅆󠆕󠅆󠇃󠇧󠅺󠅋󠄠󠆤󠄼󠅝󠆍󠄑󠄆󠅈󠇩󠅼󠅂󠆊󠄁󠆦󠅖󠅅󠆽ⷱ󠅿󠄀󠆛󠄫󠄎󠄟'[1:])))
```
or even:
```python
exec(bytes(ord(c)&255 for c in 'i󠅭󠅰󠅯󠅲󠅴󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄊󠅩󠅭󠅰󠅯󠅲󠅴󠄠󠅯󠅳󠄊󠅩󠅭󠅰󠅯󠅲󠅴󠄠󠅲󠅥󠄊󠅩󠅭󠅰󠅯󠅲󠅴󠄠󠅳󠅹󠅳󠄊󠅣󠅬󠅡󠅳󠅳󠄠󠅉󠅮󠅳󠅰󠅥󠅣󠅴󠅃󠅯󠅮󠅦󠅩󠅧󠄺󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅩󠅮󠅩󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅳󠅨󠅯󠅲󠅴󠄬󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄬󠄠󠅮󠅯󠅤󠅯󠅣󠅳󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅣󠅯󠅤󠅥󠄬󠄠󠅣󠅡󠅬󠅬󠅥󠅲󠄬󠄠󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄩󠄺󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅳󠅨󠅯󠅲󠅴󠄽󠅳󠅨󠅯󠅲󠅴󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠄽󠅤󠅵󠅮󠅤󠅥󠅲󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅮󠅯󠅤󠅯󠅣󠅳󠄽󠅮󠅯󠅤󠅯󠅣󠅳󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅬󠅯󠅮󠅧󠄽󠅬󠅯󠅮󠅧󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅣󠅯󠅤󠅥󠄽󠅣󠅯󠅤󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅣󠅡󠅬󠅬󠅥󠅲󠄽󠅣󠅡󠅬󠅬󠅥󠅲󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄽󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄊󠅣󠅬󠅡󠅳󠅳󠄠󠅉󠅮󠅳󠅰󠅥󠅣󠅴󠅁󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠄺󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅩󠅮󠅩󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅮󠅡󠅭󠅥󠄬󠄠󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅴󠅹󠅰󠅥󠄬󠄠󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄬󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄬󠄠󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄬󠄠󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄬󠄠󠅤󠅯󠅣󠄩󠄺󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅮󠅡󠅭󠅥󠄽󠅮󠅡󠅭󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅶󠅡󠅬󠅵󠅥󠄽󠅶󠅡󠅬󠅵󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅴󠅹󠅰󠅥󠄽󠅴󠅹󠅰󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄽󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠄽󠅤󠅵󠅮󠅤󠅥󠅲󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄽󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄽󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅤󠅯󠅣󠄽󠅤󠅯󠅣󠄊󠅤󠅥󠅦󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠄨󠅯󠅢󠅪󠄬󠄠󠄪󠄬󠄠󠅳󠅨󠅯󠅲󠅴󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅮󠅯󠅤󠅯󠅣󠅳󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅣󠅯󠅤󠅥󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅣󠅡󠅬󠅬󠅥󠅲󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅰󠅵󠅢󠅬󠅩󠅣󠄽󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠅡󠅬󠅬󠄽󠅆󠅡󠅬󠅳󠅥󠄩󠄺󠄊󠄉󠅣󠅯󠅮󠅦󠅩󠅧󠄽󠅉󠅮󠅳󠅰󠅥󠅣󠅴󠅃󠅯󠅮󠅦󠅩󠅧󠄨󠅳󠅨󠅯󠅲󠅴󠄽󠅳󠅨󠅯󠅲󠅴󠄬󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄽󠅤󠅵󠅮󠅤󠅥󠅲󠄠󠅯󠅲󠄠󠅡󠅬󠅬󠄬󠄠󠅮󠅯󠅤󠅯󠅣󠅳󠄽󠅮󠅯󠅤󠅯󠅣󠅳󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅬󠅯󠅮󠅧󠄠󠅯󠅲󠄠󠅡󠅬󠅬󠄬󠄠󠅣󠅯󠅤󠅥󠄽󠅣󠅯󠅤󠅥󠄠󠅯󠅲󠄠󠅡󠅬󠅬󠄬󠄠󠅣󠅡󠅬󠅬󠅥󠅲󠄽󠅣󠅡󠅬󠅬󠅥󠅲󠄠󠅯󠅲󠄠󠅡󠅬󠅬󠄬󠄠󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄽󠅮󠅯󠅴󠄠󠅰󠅵󠅢󠅬󠅩󠅣󠄩󠄊󠄉󠅯󠅵󠅴󠅰󠅵󠅴󠄽󠅬󠅩󠅳󠅴󠄨󠅟󠅹󠅩󠅥󠅬󠅤󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅬󠅩󠅮󠅥󠅳󠄨󠅯󠅢󠅪󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄩󠄊󠄉󠅩󠅦󠄠󠅳󠅹󠅳󠄮󠅳󠅴󠅤󠅯󠅵󠅴󠄮󠅩󠅳󠅡󠅴󠅴󠅹󠄨󠄩󠄺󠄊󠄉󠄉󠅴󠅥󠅲󠅭󠅩󠅮󠅡󠅬󠅟󠅷󠅩󠅤󠅴󠅨󠄽󠅯󠅳󠄮󠅧󠅥󠅴󠅟󠅴󠅥󠅲󠅭󠅩󠅮󠅡󠅬󠅟󠅳󠅩󠅺󠅥󠄨󠄩󠄮󠅣󠅯󠅬󠅵󠅭󠅮󠅳󠄊󠄉󠄉󠅯󠅵󠅴󠅰󠅵󠅴󠄮󠅩󠅮󠅳󠅥󠅲󠅴󠄨󠄰󠄬󠄠󠅳󠅴󠅹󠅬󠅥󠄮󠅂󠅁󠅒󠄠󠄫󠄠󠄧󠇢󠆔󠆀󠄧󠄠󠄪󠄠󠅴󠅥󠅲󠅭󠅩󠅮󠅡󠅬󠅟󠅷󠅩󠅤󠅴󠅨󠄠󠄫󠄠󠅒󠅅󠅓󠅅󠅔󠄩󠄊󠄉󠄉󠅯󠅵󠅴󠅰󠅵󠅴󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅳󠅴󠅹󠅬󠅥󠄮󠅂󠅁󠅒󠄠󠄫󠄠󠄧󠇢󠆔󠆀󠄧󠄠󠄪󠄠󠅴󠅥󠅲󠅭󠅩󠅮󠅡󠅬󠅟󠅷󠅩󠅤󠅴󠅨󠄠󠄫󠄠󠅒󠅅󠅓󠅅󠅔󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠄧󠅜󠅮󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅯󠅵󠅴󠅰󠅵󠅴󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅹󠅩󠅥󠅬󠅤󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅬󠅩󠅮󠅥󠅳󠄨󠅯󠅢󠅪󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅣󠅡󠅬󠅬󠅥󠅲󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠅲󠅯󠅭󠄠󠅟󠅧󠅥󠅮󠅥󠅲󠅡󠅴󠅥󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅩󠅮󠅦󠅯󠄨󠄩󠄊󠄉󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅯󠅢󠅪󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅔󠅲󠅵󠅥󠄩󠄊󠄉󠅲󠅥󠅰󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠄽󠅲󠅥󠅰󠅲󠄨󠅯󠅢󠅪󠄩󠄊󠄉󠅩󠅦󠄠󠅲󠅥󠅰󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠄠󠄽󠄽󠄠󠅳󠅴󠅲󠄨󠅯󠅢󠅪󠄩󠄠󠅯󠅲󠄠󠅲󠅥󠅰󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠄠󠄽󠄽󠄠󠅟󠅳󠅴󠅲󠅩󠅰󠅟󠅣󠅯󠅬󠅯󠅲󠄨󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠄩󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅶󠅡󠅬󠅵󠅥󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠅽󠄧󠄊󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅳󠅴󠅲󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠅽󠄧󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅲󠅥󠅰󠅲󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅈󠅅󠅁󠅄󠅽󠅻󠅲󠅥󠅰󠅲󠅟󠅶󠅡󠅬󠅵󠅥󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅳󠅴󠅲󠅟󠅴󠅹󠅰󠅥󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅴󠅹󠅰󠅥󠄨󠅴󠅹󠅰󠅥󠄨󠅯󠅢󠅪󠄩󠄩󠄊󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅴󠅹󠅰󠅥󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅳󠅴󠅲󠅟󠅴󠅹󠅰󠅥󠅽󠄧󠄊󠄉󠅰󠅡󠅲󠅥󠅮󠅴󠅳󠄽󠄧󠄬󠄠󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅟󠅧󠅥󠅴󠅟󠅰󠅡󠅲󠅥󠅮󠅴󠅟󠅴󠅹󠅰󠅥󠅳󠄨󠅴󠅹󠅰󠅥󠄨󠅯󠅢󠅪󠄩󠄩󠄩󠄊󠄉󠅩󠅦󠄠󠅰󠅡󠅲󠅥󠅮󠅴󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅰󠅡󠅲󠅥󠅮󠅴󠅳󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅰󠅡󠅲󠅥󠅮󠅴󠅳󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄨󠅧󠅥󠅴󠅡󠅴󠅴󠅲󠄨󠅯󠅢󠅪󠄬󠄠󠄧󠅟󠅟󠅬󠅥󠅮󠅟󠅟󠄧󠄬󠄠󠅎󠅯󠅮󠅥󠄩󠄩󠄺󠄊󠄉󠄉󠅴󠅲󠅹󠄺󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅬󠅥󠅮󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅬󠅥󠅮󠄨󠅯󠅢󠅪󠄩󠄩󠅽󠄧󠄊󠄉󠄉󠅥󠅸󠅣󠅥󠅰󠅴󠄠󠅔󠅹󠅰󠅥󠅅󠅲󠅲󠅯󠅲󠄺󠄊󠄉󠄉󠄉󠅰󠅡󠅳󠅳󠄊󠄉󠅩󠅦󠄠󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄨󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠄉󠅮󠅡󠅭󠅥󠄽󠅧󠅥󠅴󠅡󠅴󠅴󠅲󠄨󠅯󠅢󠅪󠄬󠄠󠄧󠅟󠅟󠅮󠅡󠅭󠅥󠅟󠅟󠄧󠄬󠄠󠄧󠇢󠆀󠆦󠄧󠄩󠄊󠄉󠄉󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄽󠅟󠅧󠅥󠅴󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄨󠅮󠅡󠅭󠅥󠄬󠄠󠅯󠅢󠅪󠄩󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅽󠄧󠄊󠄉󠅤󠅯󠅣󠄽󠅟󠅧󠅥󠅴󠅟󠅤󠅯󠅣󠄨󠅯󠅢󠅪󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅔󠅲󠅵󠅥󠄩󠄊󠄉󠅩󠅦󠄠󠅤󠅯󠅣󠄠󠅡󠅮󠅤󠄠󠄨󠅮󠅯󠅴󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅮󠅯󠅤󠅯󠅣󠅳󠄩󠄠󠅡󠅮󠅤󠄠󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄨󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅤󠅯󠅣󠄮󠅣󠅯󠅵󠅮󠅴󠄨󠄧󠅜󠅮󠄧󠄩󠄠󠄽󠄽󠄠󠄰󠄺󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅄󠅏󠅃󠅓󠅽󠄢󠄢󠄢󠅻󠅤󠅯󠅣󠅽󠄢󠄢󠄢󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠅲󠅯󠅭󠄠󠅛󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅄󠅏󠅃󠅓󠅽󠄢󠄢󠄢󠄧󠄬󠄠󠅤󠅯󠅣󠄬󠄠󠅦󠄧󠄢󠄢󠄢󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠅝󠄊󠄉󠅩󠅦󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅣󠅯󠅤󠅥󠄠󠅡󠅮󠅤󠄠󠄨󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅩󠅳󠅣󠅬󠅡󠅳󠅳󠄨󠅯󠅢󠅪󠄩󠄠󠅯󠅲󠄠󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄨󠅯󠅢󠅪󠄩󠄩󠄺󠄊󠄉󠄉󠅳󠅯󠅵󠅲󠅣󠅥󠄽󠅟󠅧󠅥󠅴󠅟󠅳󠅯󠅵󠅲󠅣󠅥󠅟󠅣󠅯󠅤󠅥󠄨󠅯󠅢󠅪󠄩󠄊󠄉󠄉󠅩󠅦󠄠󠅳󠅯󠅵󠅲󠅣󠅥󠄺󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅳󠅯󠅵󠅲󠅣󠅥󠄠󠅣󠅯󠅤󠅥󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅜󠅮󠅻󠅳󠅯󠅵󠅲󠅣󠅥󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅳󠅨󠅯󠅲󠅴󠄺󠄊󠄉󠄉󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄽󠅳󠅯󠅲󠅴󠅥󠅤󠄨󠅟󠅩󠅴󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄨󠅯󠅢󠅪󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄬󠄠󠅫󠅥󠅹󠄽󠅬󠅡󠅭󠅢󠅤󠅡󠄠󠅡󠅴󠅴󠅲󠄺󠄠󠅡󠅴󠅴󠅲󠄮󠅮󠅡󠅭󠅥󠄩󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠅲󠅯󠅭󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠅟󠅳󠅥󠅣󠅴󠅩󠅯󠅮󠅳󠄨󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅩󠅴󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄨󠅯󠅢󠅪󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄺󠄊󠄉󠅦󠅯󠅲󠄠󠅫󠅥󠅹󠄠󠅩󠅮󠄠󠅤󠅩󠅲󠄨󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠄉󠅤󠅵󠅮󠅤󠅥󠅲󠄽󠅫󠅥󠅹󠄮󠅳󠅴󠅡󠅲󠅴󠅳󠅷󠅩󠅴󠅨󠄨󠄧󠅟󠅟󠄧󠄩󠄠󠅡󠅮󠅤󠄠󠅫󠅥󠅹󠄮󠅥󠅮󠅤󠅳󠅷󠅩󠅴󠅨󠄨󠄧󠅟󠅟󠄧󠄩󠄊󠄉󠄉󠅩󠅦󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄠󠅡󠅮󠅤󠄠󠄨󠅮󠅯󠅴󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠄉󠅣󠅯󠅮󠅴󠅩󠅮󠅵󠅥󠄊󠄉󠄉󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄽󠅫󠅥󠅹󠄮󠅳󠅴󠅡󠅲󠅴󠅳󠅷󠅩󠅴󠅨󠄨󠄧󠅟󠄧󠄩󠄠󠅡󠅮󠅤󠄠󠄨󠅮󠅯󠅴󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄩󠄊󠄉󠄉󠅴󠅲󠅹󠄺󠄊󠄉󠄉󠄉󠅶󠅡󠅬󠅵󠅥󠄽󠅧󠅥󠅴󠅡󠅴󠅴󠅲󠄨󠅯󠅢󠅪󠄬󠄠󠅫󠅥󠅹󠄩󠄊󠄉󠄉󠅥󠅸󠅣󠅥󠅰󠅴󠄠󠅂󠅡󠅳󠅥󠅅󠅸󠅣󠅥󠅰󠅴󠅩󠅯󠅮󠄠󠅡󠅳󠄠󠅥󠄺󠄊󠄉󠄉󠄉󠅶󠅡󠅬󠅵󠅥󠄽󠅥󠄊󠄉󠄉󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄽󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄩󠄊󠄉󠄉󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄽󠅟󠅧󠅥󠅴󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄨󠅫󠅥󠅹󠄬󠄠󠅶󠅡󠅬󠅵󠅥󠄩󠄠󠅩󠅦󠄠󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄠󠅥󠅬󠅳󠅥󠄠󠅎󠅯󠅮󠅥󠄊󠄉󠄉󠅤󠅯󠅣󠄽󠅟󠅧󠅥󠅴󠅟󠅤󠅯󠅣󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅬󠅯󠅮󠅧󠄩󠄠󠅩󠅦󠄠󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄠󠅥󠅬󠅳󠅥󠄠󠅎󠅯󠅮󠅥󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅉󠅮󠅳󠅰󠅥󠅣󠅴󠅁󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠄨󠅮󠅡󠅭󠅥󠄽󠅫󠅥󠅹󠄬󠄠󠅶󠅡󠅬󠅵󠅥󠄽󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅴󠅹󠅰󠅥󠄽󠅴󠅹󠅰󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄩󠄬󠄠󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄽󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠄬󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄽󠅤󠅵󠅮󠅤󠅥󠅲󠄬󠄠󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄽󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄬󠄠󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄽󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄬󠄠󠅤󠅯󠅣󠄽󠅤󠅯󠅣󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅧󠅥󠅴󠅟󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄨󠅮󠅡󠅭󠅥󠄬󠄠󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠅴󠅲󠅹󠄺󠄊󠄉󠄉󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄨󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄨󠅯󠅢󠅪󠄩󠄩󠄊󠄉󠅥󠅸󠅣󠅥󠅰󠅴󠄠󠄨󠅖󠅡󠅬󠅵󠅥󠅅󠅲󠅲󠅯󠅲󠄬󠄠󠅔󠅹󠅰󠅥󠅅󠅲󠅲󠅯󠅲󠄩󠄺󠄊󠄉󠄉󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄽󠅦󠄧󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄨󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠇢󠆀󠆦󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄩󠄧󠄊󠄉󠅩󠅦󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅩󠅳󠅣󠅬󠅡󠅳󠅳󠄨󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠄉󠅰󠅲󠅥󠅦󠅩󠅸󠄽󠄧󠅣󠅬󠅡󠅳󠅳󠄠󠄧󠄊󠄉󠅥󠅬󠅩󠅦󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅩󠅳󠅣󠅯󠅲󠅯󠅵󠅴󠅩󠅮󠅥󠅦󠅵󠅮󠅣󠅴󠅩󠅯󠅮󠄨󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠄉󠅰󠅲󠅥󠅦󠅩󠅸󠄽󠄧󠅡󠅳󠅹󠅮󠅣󠄠󠅤󠅥󠅦󠄠󠄧󠄊󠄉󠅥󠅬󠅩󠅦󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅩󠅳󠅦󠅵󠅮󠅣󠅴󠅩󠅯󠅮󠄨󠅯󠅢󠅪󠄩󠄠󠅯󠅲󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅩󠅳󠅭󠅥󠅴󠅨󠅯󠅤󠄨󠅯󠅢󠅪󠄩󠄠󠅯󠅲󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅩󠅳󠅢󠅵󠅩󠅬󠅴󠅩󠅮󠄨󠅯󠅢󠅪󠄩󠄠󠅯󠅲󠄠󠅨󠅡󠅳󠅡󠅴󠅴󠅲󠄨󠅯󠅢󠅪󠄬󠄠󠄧󠅟󠅟󠅮󠅡󠅭󠅥󠅟󠅟󠄧󠄩󠄺󠄊󠄉󠄉󠅰󠅲󠅥󠅦󠅩󠅸󠄽󠄧󠅤󠅥󠅦󠄠󠄧󠄊󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠅰󠅲󠅥󠅦󠅩󠅸󠄽󠄧󠄧󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅋󠅅󠅙󠅗󠅏󠅒󠅄󠅽󠅻󠅰󠅲󠅥󠅦󠅩󠅸󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅁󠅌󠅌󠅁󠅂󠅌󠅅󠅽󠅻󠅮󠅡󠅭󠅥󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅻󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄨󠅳󠅩󠅧󠄩󠄺󠄊󠄉󠅰󠅡󠅲󠅴󠅳󠄽󠅛󠅝󠄊󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅰󠅯󠅳󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄽󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅫󠅷󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄽󠅔󠅲󠅵󠅥󠄊󠄉󠅦󠅯󠅲󠄠󠅰󠅡󠅲󠅡󠅭󠄠󠅩󠅮󠄠󠅳󠅩󠅧󠄮󠅰󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠅳󠄮󠅶󠅡󠅬󠅵󠅥󠅳󠄨󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅫󠅩󠅮󠅤󠄠󠄽󠄽󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅐󠅏󠅓󠅉󠅔󠅉󠅏󠅎󠅁󠅌󠅟󠅏󠅎󠅌󠅙󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅰󠅯󠅳󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄽󠅔󠅲󠅵󠅥󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅰󠅯󠅳󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄺󠄊󠄉󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄯󠄧󠄩󠄊󠄉󠄉󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅰󠅯󠅳󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄽󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠄉󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅫󠅩󠅮󠅤󠄠󠄽󠄽󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅖󠅁󠅒󠅟󠅐󠅏󠅓󠅉󠅔󠅉󠅏󠅎󠅁󠅌󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅫󠅷󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄽󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅫󠅩󠅮󠅤󠄠󠄽󠄽󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅋󠅅󠅙󠅗󠅏󠅒󠅄󠅟󠅏󠅎󠅌󠅙󠄠󠅡󠅮󠅤󠄠󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅫󠅷󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄺󠄊󠄉󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄪󠄧󠄩󠄊󠄉󠄉󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅫󠅷󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄽󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅟󠅰󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄨󠅰󠅡󠅲󠅡󠅭󠄩󠄩󠄊󠄉󠅩󠅦󠄠󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅰󠅯󠅳󠅟󠅯󠅮󠅬󠅹󠅟󠅳󠅥󠅰󠅡󠅲󠅡󠅴󠅯󠅲󠄺󠄊󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄯󠄧󠄩󠄊󠄉󠅡󠅲󠅧󠅳󠅟󠅳󠅴󠅲󠄽󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄬󠄠󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅰󠅡󠅲󠅴󠅳󠄩󠄊󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅥󠅤󠄽󠅦󠄧󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄨󠅻󠅡󠅲󠅧󠅳󠅟󠅳󠅴󠅲󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄩󠄧󠄊󠄉󠅩󠅦󠄠󠅳󠅩󠅧󠄮󠅲󠅥󠅴󠅵󠅲󠅮󠅟󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄠󠅩󠅳󠄠󠅮󠅯󠅴󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅓󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄮󠅥󠅭󠅰󠅴󠅹󠄺󠄊󠄉󠄉󠅲󠅥󠅮󠅤󠅥󠅲󠅥󠅤󠄠󠄫󠄽󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄠󠄭󠄾󠄠󠅻󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄨󠅳󠅩󠅧󠄮󠅲󠅥󠅴󠅵󠅲󠅮󠅟󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄩󠅽󠄧󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅲󠅥󠅮󠅤󠅥󠅲󠅥󠅤󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅟󠅰󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄨󠅰󠅡󠅲󠅡󠅭󠄩󠄺󠄊󠄉󠅰󠅡󠅲󠅴󠅳󠄽󠅛󠅝󠄊󠄉󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅫󠅩󠅮󠅤󠄠󠄽󠄽󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅖󠅁󠅒󠅟󠅐󠅏󠅓󠅉󠅔󠅉󠅏󠅎󠅁󠅌󠄺󠄊󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄪󠄧󠄩󠄊󠄉󠅥󠅬󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅫󠅩󠅮󠅤󠄠󠄽󠄽󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅖󠅁󠅒󠅟󠅋󠅅󠅙󠅗󠅏󠅒󠅄󠄺󠄊󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄪󠄪󠄧󠄩󠄊󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅖󠅁󠅒󠅉󠅁󠅂󠅌󠅅󠅽󠅻󠅰󠅡󠅲󠅡󠅭󠄮󠅮󠅡󠅭󠅥󠅽󠄧󠄩󠄊󠄉󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄠󠅩󠅳󠄠󠅮󠅯󠅴󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅥󠅭󠅰󠅴󠅹󠄺󠄊󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄺󠄠󠅻󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄨󠅰󠅡󠅲󠅡󠅭󠄮󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄩󠅽󠄧󠄩󠄊󠄉󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅤󠅥󠅦󠅡󠅵󠅬󠅴󠄠󠅩󠅳󠄠󠅮󠅯󠅴󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅥󠅭󠅰󠅴󠅹󠄺󠄊󠄉󠄉󠅥󠅱󠅵󠅡󠅬󠅳󠄠󠄽󠄠󠄧󠄽󠄧󠄠󠅩󠅦󠄠󠅰󠅡󠅲󠅡󠅭󠄮󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄠󠅩󠅳󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅐󠅡󠅲󠅡󠅭󠅥󠅴󠅥󠅲󠄮󠅥󠅭󠅰󠅴󠅹󠄠󠅥󠅬󠅳󠅥󠄠󠄧󠄠󠄽󠄠󠄧󠄊󠄉󠄉󠅰󠅡󠅲󠅴󠅳󠄮󠅡󠅰󠅰󠅥󠅮󠅤󠄨󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅥󠅱󠅵󠅡󠅬󠅳󠅽󠅻󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅰󠅡󠅲󠅡󠅭󠄮󠅤󠅥󠅦󠅡󠅵󠅬󠅴󠄩󠅽󠄧󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠄧󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅰󠅡󠅲󠅴󠅳󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄨󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅧󠅥󠅴󠅡󠅴󠅴󠅲󠄨󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄬󠄠󠄧󠅟󠅟󠅭󠅯󠅤󠅵󠅬󠅥󠅟󠅟󠄧󠄬󠄠󠅎󠅯󠅮󠅥󠄩󠄠󠄽󠄽󠄠󠄧󠅴󠅹󠅰󠅩󠅮󠅧󠄧󠄺󠄊󠄉󠄉󠅤󠅥󠅦󠄠󠅲󠅥󠅰󠅬󠄨󠅭󠅡󠅴󠅣󠅨󠄩󠄺󠄊󠄉󠄉󠄉󠅩󠅦󠄠󠅭󠅡󠅴󠅣󠅨󠄮󠅧󠅲󠅯󠅵󠅰󠄨󠄩󠄮󠅳󠅴󠅡󠅲󠅴󠅳󠅷󠅩󠅴󠅨󠄨󠄧󠅴󠅹󠅰󠅩󠅮󠅧󠄮󠄧󠄩󠄺󠄊󠄉󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅭󠅡󠅴󠅣󠅨󠄮󠅧󠅲󠅯󠅵󠅰󠄨󠄩󠅛󠅬󠅥󠅮󠄨󠄧󠅴󠅹󠅰󠅩󠅮󠅧󠄮󠄧󠄩󠄺󠅝󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅭󠅡󠅴󠅣󠅨󠄮󠅧󠅲󠅯󠅵󠅰󠄨󠄩󠄊󠄉󠄉󠅮󠅡󠅭󠅥󠄽󠅲󠅥󠄮󠅳󠅵󠅢󠄨󠄧󠅛󠅜󠅜󠅷󠅜󠅜󠄮󠅝󠄫󠄧󠄬󠄠󠅲󠅥󠅰󠅬󠄬󠄠󠅲󠅥󠅰󠅲󠄨󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄩󠄩󠄊󠄉󠅥󠅬󠅩󠅦󠄠󠅧󠅥󠅴󠅡󠅴󠅴󠅲󠄨󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄬󠄠󠄧󠅟󠅟󠅮󠅡󠅭󠅥󠅟󠅟󠄧󠄬󠄠󠅎󠅯󠅮󠅥󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅴󠅹󠅰󠅥󠄨󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄩󠄊󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠅮󠅡󠅭󠅥󠄽󠅲󠅥󠅰󠅲󠄨󠅡󠅮󠅮󠅯󠅴󠅡󠅴󠅩󠅯󠅮󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅮󠅡󠅭󠅥󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅧󠅥󠅴󠅟󠅳󠅯󠅵󠅲󠅣󠅥󠅟󠅣󠅯󠅤󠅥󠄨󠅯󠅢󠅪󠄩󠄺󠄊󠄉󠅴󠅲󠅹󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅧󠅥󠅴󠅳󠅯󠅵󠅲󠅣󠅥󠄨󠅯󠅢󠅪󠄩󠄊󠄉󠅥󠅸󠅣󠅥󠅰󠅴󠄠󠄨󠅏󠅓󠅅󠅲󠅲󠅯󠅲󠄬󠄠󠅔󠅹󠅰󠅥󠅅󠅲󠅲󠅯󠅲󠄬󠄠󠅉󠅮󠅤󠅥󠅮󠅴󠅡󠅴󠅩󠅯󠅮󠅅󠅲󠅲󠅯󠅲󠄩󠄠󠅡󠅳󠄠󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅦󠅡󠅩󠅬󠅥󠅤󠄠󠅴󠅯󠄠󠅧󠅥󠅴󠄠󠅳󠅯󠅵󠅲󠅣󠅥󠄠󠅣󠅯󠅤󠅥󠄺󠄠󠅻󠅴󠅹󠅰󠅥󠄨󠅥󠄩󠅽󠄺󠄠󠅻󠅥󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅧󠅥󠅴󠅟󠅤󠅯󠅣󠄨󠅯󠅢󠅪󠄬󠄠󠅬󠅯󠅮󠅧󠄩󠄺󠄊󠄉󠅤󠅯󠅣󠄽󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅧󠅥󠅴󠅤󠅯󠅣󠄨󠅯󠅢󠅪󠄩󠄊󠄉󠅩󠅦󠄠󠅤󠅯󠅣󠄠󠅩󠅳󠄠󠅎󠅯󠅮󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅎󠅯󠅮󠅥󠄊󠄉󠅤󠅯󠅣󠄽󠅤󠅯󠅣󠄮󠅳󠅴󠅲󠅩󠅰󠄨󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅤󠅯󠅣󠄠󠅩󠅦󠄠󠅬󠅯󠅮󠅧󠄠󠅥󠅬󠅳󠅥󠄠󠅟󠅳󠅨󠅯󠅲󠅴󠅥󠅮󠅟󠅳󠅴󠅲󠅩󠅮󠅧󠄨󠅤󠅯󠅣󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠄨󠅡󠅴󠅴󠅲󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄺󠄊󠄉󠅶󠅡󠅬󠅵󠅥󠅟󠅳󠅴󠅲󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅡󠅴󠅴󠅲󠄮󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅬󠅯󠅮󠅧󠄩󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅬󠅯󠅮󠅧󠄺󠄊󠄉󠄉󠅶󠅡󠅬󠅵󠅥󠅟󠅳󠅴󠅲󠄽󠅟󠅳󠅨󠅯󠅲󠅴󠅥󠅮󠅟󠅳󠅴󠅲󠅩󠅮󠅧󠄨󠅶󠅡󠅬󠅵󠅥󠅟󠅳󠅴󠅲󠄩󠄊󠄉󠅴󠅹󠅰󠅥󠅟󠅳󠅴󠅲󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅴󠅹󠅰󠅥󠄨󠅡󠅴󠅴󠅲󠄮󠅴󠅹󠅰󠅥󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅖󠅁󠅒󠅉󠅁󠅂󠅌󠅅󠅽󠅻󠅡󠅴󠅴󠅲󠄮󠅮󠅡󠅭󠅥󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄺󠄠󠅻󠅴󠅹󠅰󠅥󠅟󠅳󠅴󠅲󠅽󠄠󠄽󠄠󠅻󠅶󠅡󠅬󠅵󠅥󠅟󠅳󠅴󠅲󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅳󠅨󠅯󠅲󠅴󠅥󠅮󠅟󠅳󠅴󠅲󠅩󠅮󠅧󠄨󠅴󠅥󠅸󠅴󠄩󠄺󠄊󠄉󠅦󠅩󠅲󠅳󠅴󠅟󠅬󠅩󠅮󠅥󠄬󠄠󠅟󠄬󠄠󠅲󠅥󠅳󠅴󠄽󠅴󠅥󠅸󠅴󠄮󠅰󠅡󠅲󠅴󠅩󠅴󠅩󠅯󠅮󠄨󠄧󠅜󠅮󠄧󠄩󠄊󠄉󠅩󠅦󠄠󠅲󠅥󠅳󠅴󠄠󠅯󠅲󠄠󠅬󠅥󠅮󠄨󠅟󠅳󠅴󠅲󠅩󠅰󠅟󠅣󠅯󠅬󠅯󠅲󠄨󠅦󠅩󠅲󠅳󠅴󠅟󠅬󠅩󠅮󠅥󠄩󠄩󠄠󠄾󠄠󠄱󠄰󠄰󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠅩󠅲󠅳󠅴󠅟󠅬󠅩󠅮󠅥󠅛󠄺󠄱󠄰󠄰󠅝󠄠󠄫󠄠󠅒󠅅󠅓󠅅󠅔󠄠󠄫󠄠󠄧󠇢󠆀󠆦󠄧󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠅩󠅲󠅳󠅴󠅟󠅬󠅩󠅮󠅥󠄊󠅤󠅥󠅦󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅟󠅭󠅥󠅴󠅨󠅯󠅤󠄨󠅡󠅴󠅴󠅲󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅡󠅴󠅴󠅲󠄮󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠄠󠄠󠅻󠅡󠅴󠅴󠅲󠄮󠅮󠅡󠅭󠅥󠅽󠄨󠇢󠆀󠆦󠄩󠄧󠄊󠄉󠅩󠅦󠄠󠅡󠅴󠅴󠅲󠄮󠅤󠅯󠅣󠄠󠅡󠅮󠅤󠄠󠄨󠅮󠅯󠅴󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅮󠅯󠅤󠅯󠅣󠅳󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅡󠅴󠅴󠅲󠄮󠅤󠅯󠅣󠄮󠅣󠅯󠅵󠅮󠅴󠄨󠄧󠅜󠅮󠄧󠄩󠄠󠄽󠄽󠄠󠄰󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠄠󠄠󠅻󠅡󠅴󠅴󠅲󠄮󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅽󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅄󠅏󠅃󠅓󠅽󠄣󠄠󠅻󠅡󠅴󠅴󠅲󠄮󠅤󠅯󠅣󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠄠󠄠󠅻󠅡󠅴󠅴󠅲󠄮󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅽󠄺󠅜󠅮󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅄󠅏󠅃󠅓󠅽󠄢󠄢󠄢󠅜󠅮󠅻󠅡󠅴󠅴󠅲󠄮󠅤󠅯󠅣󠅽󠅜󠅮󠄢󠄢󠄢󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠄠󠄠󠅻󠅡󠅴󠅴󠅲󠄮󠅳󠅩󠅧󠅮󠅡󠅴󠅵󠅲󠅥󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄽󠅔󠅲󠅵󠅥󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄽󠄰󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅩󠅳󠅩󠅮󠅳󠅴󠅡󠅮󠅣󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅳󠅴󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄢󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄧󠅻󠅶󠅡󠅬󠅵󠅥󠅽󠄧󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄢󠄊󠄉󠅩󠅦󠄠󠅶󠅡󠅬󠅵󠅥󠄠󠅩󠅳󠄠󠅎󠅯󠅮󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅎󠅏󠅎󠅅󠅽󠅎󠅯󠅮󠅥󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅶󠅡󠅬󠅵󠅥󠄠󠅩󠅳󠄠󠅔󠅲󠅵󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅕󠅅󠅽󠅔󠅲󠅵󠅥󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅶󠅡󠅬󠅵󠅥󠄠󠅩󠅳󠄠󠅆󠅡󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅆󠅁󠅌󠅓󠅅󠅽󠅆󠅡󠅬󠅳󠅥󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅩󠅳󠅩󠅮󠅳󠅴󠅡󠅮󠅣󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠄨󠅩󠅮󠅴󠄬󠄠󠅦󠅬󠅯󠅡󠅴󠄩󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅎󠅕󠅍󠅂󠅅󠅒󠅽󠅻󠅶󠅡󠅬󠅵󠅥󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅩󠅳󠅩󠅮󠅳󠅴󠅡󠅮󠅣󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅤󠅩󠅣󠅴󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅤󠅩󠅣󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄫󠄠󠄱󠄩󠄊󠄉󠅩󠅦󠄠󠅩󠅳󠅩󠅮󠅳󠅴󠅡󠅮󠅣󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅬󠅩󠅳󠅴󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅬󠅩󠅳󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅶󠅡󠅬󠅵󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄫󠄠󠄱󠄩󠄊󠄉󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠄽󠅳󠅴󠅲󠄨󠅶󠅡󠅬󠅵󠅥󠄩󠄊󠄉󠅡󠅮󠅧󠅬󠅥󠅟󠅢󠅲󠅡󠅣󠅫󠅥󠅴󠅟󠅭󠅡󠅴󠅣󠅨󠄽󠅲󠅥󠄮󠅦󠅵󠅬󠅬󠅭󠅡󠅴󠅣󠅨󠄨󠄧󠄼󠄨󠄮󠄪󠄩󠄾󠄧󠄬󠄠󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠄩󠄊󠄉󠅩󠅦󠄠󠅡󠅮󠅧󠅬󠅥󠅟󠅢󠅲󠅡󠅣󠅫󠅥󠅴󠅟󠅭󠅡󠅴󠅣󠅨󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄼󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅖󠅁󠅒󠅉󠅁󠅂󠅌󠅅󠅽󠅻󠅡󠅮󠅧󠅬󠅥󠅟󠅢󠅲󠅡󠅣󠅫󠅥󠅴󠅟󠅭󠅡󠅴󠅣󠅨󠄮󠅧󠅲󠅯󠅵󠅰󠄨󠄱󠄩󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄾󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠅻󠅳󠅴󠅲󠅟󠅶󠅡󠅬󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅤󠅩󠅣󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅤󠅩󠅣󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄾󠄠󠄳󠄰󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅆󠅁󠅌󠅓󠅅󠅽󠅅󠅒󠅒󠅏󠅒󠄺󠄠󠅴󠅯󠅯󠄠󠅤󠅥󠅥󠅰󠅬󠅹󠄠󠅮󠅥󠅳󠅴󠅥󠅤󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅬󠅥󠅮󠄨󠅤󠅩󠅣󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅻󠅽󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅴󠅥󠅭󠅳󠄽󠄨󠅦󠄧󠅻󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅫󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄩󠅽󠄺󠄠󠅻󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅶󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄩󠅽󠄧󠄠󠅦󠅯󠅲󠄠󠅫󠄬󠄠󠅶󠄠󠅩󠅮󠄠󠅤󠅩󠅣󠄮󠅩󠅴󠅥󠅭󠅳󠄨󠄩󠄩󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅬󠅯󠅮󠅧󠄺󠄊󠄉󠄉󠅩󠅴󠅥󠅭󠅳󠅟󠅳󠅴󠅲󠄽󠄧󠄬󠄠󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅩󠅴󠅥󠅭󠅳󠄩󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅻󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅻󠅩󠅴󠅥󠅭󠅳󠅟󠅳󠅴󠅲󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅽󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅬󠅩󠅮󠅥󠅳󠄽󠄧󠅜󠅮󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠄨󠄧󠄉󠄧󠄠󠄪󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄫󠄠󠅦󠄧󠅻󠅩󠅴󠅽󠄬󠄧󠄠󠅦󠅯󠅲󠄠󠅩󠅴󠄠󠅩󠅮󠄠󠅩󠅴󠅥󠅭󠅳󠄩󠄩󠄊󠄉󠅥󠅮󠅤󠅟󠅩󠅮󠅤󠅥󠅮󠅴󠄽󠄧󠄉󠄧󠄠󠄪󠄠󠄨󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄭󠄠󠄱󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅻󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅜󠅮󠅻󠅬󠅩󠅮󠅥󠅳󠅽󠅜󠅮󠅻󠅥󠅮󠅤󠅟󠅩󠅮󠅤󠅥󠅮󠅴󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅽󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅬󠅩󠅳󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅬󠅳󠅴󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄾󠄠󠄳󠄰󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅆󠅁󠅌󠅓󠅅󠅽󠅅󠅒󠅒󠅏󠅒󠄺󠄠󠅴󠅯󠅯󠄠󠅤󠅥󠅥󠅰󠅬󠅹󠄠󠅮󠅥󠅳󠅴󠅥󠅤󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅬󠅥󠅮󠄨󠅬󠅳󠅴󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅛󠅝󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅩󠅴󠅥󠅭󠅳󠄽󠄨󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅶󠅡󠅬󠄬󠄠󠅬󠅯󠅮󠅧󠄬󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄩󠄠󠅦󠅯󠅲󠄠󠅶󠅡󠅬󠄠󠅩󠅮󠄠󠅬󠅳󠅴󠄩󠄊󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅬󠅯󠅮󠅧󠄺󠄊󠄉󠄉󠅩󠅴󠅥󠅭󠅳󠅟󠅳󠅴󠅲󠄽󠄧󠄬󠄠󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅩󠅴󠅥󠅭󠅳󠄩󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅛󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅻󠅩󠅴󠅥󠅭󠅳󠅟󠅳󠅴󠅲󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅝󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅬󠅩󠅮󠅥󠅳󠄽󠄧󠅜󠅮󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠄨󠄧󠄉󠄧󠄠󠄪󠄠󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄫󠄠󠅦󠄧󠅻󠅩󠅴󠅽󠄬󠄧󠄠󠅦󠅯󠅲󠄠󠅩󠅴󠄠󠅩󠅮󠄠󠅩󠅴󠅥󠅭󠅳󠄩󠄩󠄊󠄉󠅥󠅮󠅤󠅟󠅩󠅮󠅤󠅥󠅮󠅴󠄽󠄧󠄉󠄧󠄠󠄪󠄠󠄨󠅩󠅮󠅤󠅥󠅮󠅴󠄠󠄭󠄠󠄱󠄩󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅛󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅜󠅮󠅻󠅬󠅩󠅮󠅥󠅳󠅽󠅜󠅮󠅻󠅥󠅮󠅤󠅟󠅩󠅮󠅤󠅥󠅮󠅴󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅝󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅴󠅹󠅰󠅥󠄨󠅴󠅹󠅰󠅥󠅟󠄩󠄺󠄊󠄉󠅭󠅯󠅤󠅵󠅬󠅥󠄽󠅴󠅹󠅰󠅥󠅟󠄮󠅟󠅟󠅭󠅯󠅤󠅵󠅬󠅥󠅟󠅟󠄊󠄉󠅩󠅦󠄠󠅭󠅯󠅤󠅵󠅬󠅥󠄠󠅩󠅳󠄠󠅎󠅯󠅮󠅥󠄠󠅯󠅲󠄠󠅭󠅯󠅤󠅵󠅬󠅥󠄠󠄽󠄽󠄠󠅳󠅴󠅲󠄮󠅟󠅟󠅣󠅬󠅡󠅳󠅳󠅟󠅟󠄮󠅟󠅟󠅭󠅯󠅤󠅵󠅬󠅥󠅟󠅟󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅴󠅹󠅰󠅥󠅟󠄮󠅟󠅟󠅮󠅡󠅭󠅥󠅟󠅟󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅭󠅯󠅤󠅵󠅬󠅥󠅽󠄮󠅻󠅴󠅹󠅰󠅥󠅟󠄮󠅟󠅟󠅮󠅡󠅭󠅥󠅟󠅟󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅧󠅥󠅴󠅟󠅰󠅡󠅲󠅥󠅮󠅴󠅟󠅴󠅹󠅰󠅥󠅳󠄨󠅴󠅹󠅰󠅥󠅟󠄩󠄺󠄊󠄉󠅩󠅦󠄠󠅨󠅡󠅳󠅡󠅴󠅴󠅲󠄨󠅴󠅹󠅰󠅥󠅟󠄬󠄠󠄧󠅟󠅟󠅭󠅲󠅯󠅟󠅟󠄧󠄩󠄺󠄊󠄉󠄉󠅦󠅯󠅲󠄠󠅩󠅮󠅤󠅥󠅸󠄬󠄠󠅢󠅡󠅳󠅥󠅟󠅴󠅹󠅰󠅥󠄠󠅩󠅮󠄠󠅥󠅮󠅵󠅭󠅥󠅲󠅡󠅴󠅥󠄨󠅴󠅹󠅰󠅥󠅟󠄮󠅟󠅟󠅭󠅲󠅯󠅟󠅟󠄩󠄺󠄊󠄉󠄉󠄉󠅩󠅦󠄠󠅩󠅮󠅤󠅥󠅸󠄠󠄽󠄽󠄠󠄰󠄠󠅯󠅲󠄠󠅢󠅡󠅳󠅥󠅟󠅴󠅹󠅰󠅥󠄠󠅩󠅳󠄠󠅯󠅢󠅪󠅥󠅣󠅴󠄺󠄊󠄉󠄉󠄉󠄉󠅣󠅯󠅮󠅴󠅩󠅮󠅵󠅥󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅴󠅹󠅰󠅥󠄨󠅢󠅡󠅳󠅥󠅟󠅴󠅹󠅰󠅥󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅧󠅥󠅮󠅥󠅲󠅡󠅴󠅥󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅩󠅮󠅦󠅯󠄨󠄩󠄺󠄊󠄉󠅦󠅲󠅡󠅭󠅥󠄽󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅳󠅴󠅡󠅣󠅫󠅟󠅦󠅲󠅡󠅭󠅥󠄨󠄶󠄩󠄊󠄉󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠄺󠄊󠄉󠄉󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄽󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅧󠅥󠅴󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄨󠅦󠅲󠅡󠅭󠅥󠄩󠄊󠄉󠄉󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄮󠅦󠅩󠅬󠅥󠅮󠅡󠅭󠅥󠄺󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅣󠅡󠅬󠅬󠅥󠅲󠄠󠅦󠅩󠅬󠅥󠄺󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅻󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄮󠅦󠅩󠅬󠅥󠅮󠅡󠅭󠅥󠅽󠄺󠅻󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄮󠅬󠅩󠅮󠅥󠅮󠅯󠅽󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠄉󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄮󠅣󠅯󠅤󠅥󠅟󠅣󠅯󠅮󠅴󠅥󠅸󠅴󠄺󠄊󠄉󠄉󠄉󠅣󠅯󠅤󠅥󠄽󠄧󠅜󠅮󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅦󠅲󠅡󠅭󠅥󠅩󠅮󠅦󠅯󠄮󠅣󠅯󠅤󠅥󠅟󠅣󠅯󠅮󠅴󠅥󠅸󠅴󠄩󠄮󠅳󠅴󠅲󠅩󠅰󠄨󠄩󠄊󠄉󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅔󠅒󠅁󠅉󠅔󠅽󠅣󠅡󠅬󠅬󠅥󠅲󠄠󠅥󠅸󠅰󠅲󠅥󠅳󠅳󠅩󠅯󠅮󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅻󠅣󠅯󠅤󠅥󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠅟󠅳󠅥󠅣󠅴󠅩󠅯󠅮󠅳󠄨󠅡󠅴󠅴󠅲󠅳󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄺󠄊󠄉󠅰󠅵󠅢󠅬󠅩󠅣󠅟󠅡󠅴󠅴󠅲󠅳󠄽󠅛󠅡󠄠󠅦󠅯󠅲󠄠󠅡󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅳󠄠󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅡󠄮󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄠󠅡󠅮󠅤󠄠󠄨󠅮󠅯󠅴󠄠󠅡󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠄩󠅝󠄊󠄉󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠅟󠅡󠅴󠅴󠅲󠅳󠄽󠅛󠅡󠄠󠅦󠅯󠅲󠄠󠅡󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅳󠄠󠅩󠅦󠄠󠅡󠄮󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠅝󠄊󠄉󠅤󠅵󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠄽󠅛󠅡󠄠󠅦󠅯󠅲󠄠󠅡󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅳󠄠󠅩󠅦󠄠󠅡󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠅝󠄊󠄉󠅩󠅦󠄠󠅰󠅵󠅢󠅬󠅩󠅣󠅟󠅡󠅴󠅴󠅲󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠅲󠅯󠅭󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠅟󠅳󠅥󠅣󠅴󠅩󠅯󠅮󠄨󠄧󠅐󠅵󠅢󠅬󠅩󠅣󠄠󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄧󠄬󠄠󠅰󠅵󠅢󠅬󠅩󠅣󠅟󠅡󠅴󠅴󠅲󠅳󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄊󠄉󠅩󠅦󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠄠󠅡󠅮󠅤󠄠󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠅟󠅡󠅴󠅴󠅲󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠅲󠅯󠅭󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠅟󠅳󠅥󠅣󠅴󠅩󠅯󠅮󠄨󠄧󠅐󠅲󠅩󠅶󠅡󠅴󠅥󠄠󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄧󠄬󠄠󠅰󠅲󠅩󠅶󠅡󠅴󠅥󠅟󠅡󠅴󠅴󠅲󠅳󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄊󠄉󠅩󠅦󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠄠󠅡󠅮󠅤󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠅲󠅯󠅭󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠅟󠅳󠅥󠅣󠅴󠅩󠅯󠅮󠄨󠄧󠅄󠅵󠅮󠅤󠅥󠅲󠄠󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄧󠄬󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅳󠅟󠅳󠅥󠅣󠅴󠅩󠅯󠅮󠄨󠅴󠅩󠅴󠅬󠅥󠄬󠄠󠅡󠅴󠅴󠅲󠅳󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄺󠄊󠄉󠅡󠅴󠅴󠅲󠅟󠅶󠅡󠅲󠅳󠄽󠅛󠅡󠄠󠅦󠅯󠅲󠄠󠅡󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅳󠄠󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅡󠄮󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠅝󠄊󠄉󠅡󠅴󠅴󠅲󠅟󠅭󠅥󠅴󠅨󠅯󠅤󠅳󠄽󠅛󠅡󠄠󠅦󠅯󠅲󠄠󠅡󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅳󠄠󠅩󠅦󠄠󠅡󠄮󠅣󠅡󠅬󠅬󠅡󠅢󠅬󠅥󠅝󠄊󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠄧󠄧󠄊󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅈󠅅󠅁󠅄󠅽󠅻󠅴󠅩󠅴󠅬󠅥󠅽󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅦󠅯󠅲󠄠󠅡󠅴󠅴󠅲󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅟󠅶󠅡󠅲󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠄨󠅡󠅴󠅴󠅲󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄊󠄉󠅩󠅦󠄠󠅡󠅴󠅴󠅲󠅟󠅶󠅡󠅲󠅳󠄠󠅡󠅮󠅤󠄠󠅡󠅴󠅴󠅲󠅟󠅭󠅥󠅴󠅨󠅯󠅤󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠄧󠄧󠄊󠄉󠅦󠅯󠅲󠄠󠅡󠅴󠅴󠅲󠄠󠅩󠅮󠄠󠅡󠅴󠅴󠅲󠅟󠅭󠅥󠅴󠅨󠅯󠅤󠅳󠄺󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅡󠅴󠅴󠅲󠅟󠅭󠅥󠅴󠅨󠅯󠅤󠄨󠅡󠅴󠅴󠅲󠄬󠄠󠅣󠅯󠅮󠅦󠅩󠅧󠄩󠄊󠅤󠅥󠅦󠄠󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅳󠅴󠅡󠅣󠅫󠅟󠅦󠅲󠅡󠅭󠅥󠄨󠅤󠅥󠅰󠅴󠅨󠄩󠄺󠄊󠄉󠅦󠅲󠅡󠅭󠅥󠄽󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄮󠅣󠅵󠅲󠅲󠅥󠅮󠅴󠅦󠅲󠅡󠅭󠅥󠄨󠄩󠄊󠄉󠅦󠅯󠅲󠄠󠅟󠄠󠅩󠅮󠄠󠅲󠅡󠅮󠅧󠅥󠄨󠅤󠅥󠅰󠅴󠅨󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠄠󠅩󠅳󠄠󠅮󠅯󠅴󠄠󠅎󠅯󠅮󠅥󠄺󠄊󠄉󠄉󠄉󠅦󠅲󠅡󠅭󠅥󠄽󠅦󠅲󠅡󠅭󠅥󠄮󠅦󠅟󠅢󠅡󠅣󠅫󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅦󠅲󠅡󠅭󠅥󠄊󠅤󠅥󠅦󠄠󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄨󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄬󠄠󠅴󠅩󠅴󠅬󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄩󠄺󠄊󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅈󠅅󠅁󠅄󠅽󠅻󠅴󠅩󠅴󠅬󠅥󠅽󠄺󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄧󠄊󠄉󠅦󠅯󠅲󠄠󠅮󠅡󠅭󠅥󠄠󠅩󠅮󠄠󠅳󠅯󠅲󠅴󠅥󠅤󠄨󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄮󠅫󠅥󠅹󠅳󠄨󠄩󠄩󠄺󠄊󠄉󠄉󠅶󠅡󠅬󠅵󠅥󠅟󠅳󠅴󠅲󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅶󠅡󠅬󠅵󠅥󠄨󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠅛󠅮󠅡󠅭󠅥󠅝󠄬󠄠󠅬󠅯󠅮󠅧󠄩󠄊󠄉󠄉󠅴󠅹󠅰󠅥󠅟󠅳󠅴󠅲󠄽󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠅟󠅴󠅹󠅰󠅥󠄨󠅴󠅹󠅰󠅥󠄨󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠅛󠅮󠅡󠅭󠅥󠅝󠄩󠄩󠄊󠄉󠄉󠅹󠅩󠅥󠅬󠅤󠄠󠅦󠄧󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅖󠅁󠅒󠅉󠅁󠅂󠅌󠅅󠅽󠅻󠅮󠅡󠅭󠅥󠅽󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠄺󠄠󠅻󠅴󠅹󠅰󠅥󠅟󠅳󠅴󠅲󠅽󠄠󠄽󠄠󠅻󠅶󠅡󠅬󠅵󠅥󠅟󠅳󠅴󠅲󠅽󠄧󠄊󠅤󠅥󠅦󠄠󠅟󠅳󠅴󠅲󠅩󠅰󠅟󠅣󠅯󠅬󠅯󠅲󠄨󠅴󠅥󠅸󠅴󠄩󠄺󠄊󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅲󠅥󠄮󠅳󠅵󠅢󠄨󠄧󠅜󠅜󠅸󠄱󠅢󠅜󠅜󠅛󠅜󠅜󠅤󠄫󠄨󠄻󠅜󠅜󠅤󠄫󠄩󠄿󠅭󠄧󠄬󠄠󠄧󠄧󠄬󠄠󠅴󠅥󠅸󠅴󠄩󠄊󠅣󠅬󠅡󠅳󠅳󠄠󠅗󠅡󠅴󠄺󠄊󠄉󠄢󠄢󠄢󠅉󠅮󠅳󠅰󠅥󠅣󠅴󠅯󠅲󠄠󠅩󠅮󠅳󠅴󠅡󠅮󠅣󠅥󠄠󠅴󠅯󠄠󠅥󠅸󠅡󠅭󠅩󠅮󠅥󠄠󠅵󠅮󠅫󠅮󠅯󠅷󠅮󠄠󠅯󠅢󠅪󠅥󠅣󠅴󠅳󠄢󠄢󠄢󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅩󠅮󠅩󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠄪󠄪󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄺󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄽󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄽󠅻󠅽󠄊󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅩󠅮󠅟󠅰󠅲󠅯󠅧󠅲󠅥󠅳󠅳󠄽󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅲󠅥󠅰󠅲󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅷󠅡󠅴󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅩󠅮󠅟󠅰󠅲󠅯󠅧󠅲󠅥󠅳󠅳󠄺󠄊󠄉󠄉󠄉󠅳󠅥󠅬󠅦󠄮󠅟󠅰󠅲󠅩󠅮󠅴󠅟󠅨󠅥󠅬󠅰󠄨󠄩󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠄧󠄧󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅳󠅴󠅲󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠄧󠄼󠅗󠅁󠅔󠄠󠅉󠅮󠅳󠅰󠅥󠅣󠅴󠅯󠅲󠄠󠅯󠅢󠅪󠅥󠅣󠅴󠄾󠄧󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅰󠅲󠅩󠅮󠅴󠅟󠅨󠅥󠅬󠅰󠄨󠅳󠅥󠅬󠅦󠄩󠄺󠄊󠄉󠄉󠅴󠅥󠅸󠅴󠄽󠅦󠄧󠅔󠅲󠅹󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅷󠅡󠅴󠄠󠄯󠄠󠅯󠅢󠅪󠅥󠅣󠅴󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅯󠅲󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅷󠅡󠅴󠄮󠅭󠅯󠅤󠅩󠅦󠅩󠅥󠅲󠅳󠄠󠄯󠄠󠅯󠅢󠅪󠅥󠅣󠅴󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄠󠅡󠅮󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅯󠅢󠅪󠅥󠅣󠅴󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄮󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅈󠅅󠅁󠅄󠅽󠅍󠅯󠅤󠅩󠅦󠅩󠅥󠅲󠅳󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅡󠅲󠅥󠄺󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅳󠅨󠅯󠅲󠅴󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅯󠅲󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅳󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅨󠅩󠅤󠅥󠄠󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠄠󠄨󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄠󠅡󠅮󠅤󠄠󠅭󠅥󠅴󠅨󠅯󠅤󠅳󠄩󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅤󠅵󠅮󠅤󠅥󠅲󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅰󠅲󠅩󠅮󠅴󠄠󠅤󠅵󠅮󠅤󠅥󠅲󠄠󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅬󠅯󠅮󠅧󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅰󠅲󠅩󠅮󠅴󠄠󠅮󠅯󠅮󠄭󠅡󠅢󠅢󠅲󠅥󠅶󠅩󠅡󠅴󠅥󠅤󠄠󠅶󠅡󠅬󠅵󠅥󠅳󠄠󠅡󠅮󠅤󠄠󠅤󠅯󠅣󠅵󠅭󠅥󠅮󠅴󠅡󠅴󠅩󠅯󠅮󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅣󠅯󠅤󠅥󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅰󠅲󠅩󠅮󠅴󠄠󠅳󠅯󠅵󠅲󠅣󠅥󠄠󠅣󠅯󠅤󠅥󠄠󠅯󠅦󠄠󠅡󠄠󠅦󠅵󠅮󠅣󠅴󠅩󠅯󠅮󠄬󠄠󠅭󠅥󠅴󠅨󠅯󠅤󠄠󠅯󠅲󠄠󠅣󠅬󠅡󠅳󠅳󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅮󠅯󠅤󠅯󠅣󠅳󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅨󠅩󠅤󠅥󠄠󠅤󠅯󠅣󠅵󠅭󠅥󠅮󠅴󠅡󠅴󠅩󠅯󠅮󠄠󠅦󠅯󠅲󠄠󠅦󠅵󠅮󠅣󠅴󠅩󠅯󠅮󠅳󠄠󠅡󠅮󠅤󠄠󠅣󠅬󠅡󠅳󠅳󠅥󠅳󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅣󠅡󠅬󠅬󠅥󠅲󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅳󠅨󠅯󠅷󠄠󠅨󠅯󠅷󠄠󠅡󠅮󠅤󠄠󠅷󠅨󠅥󠅲󠅥󠄠󠅴󠅨󠅥󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅩󠅯󠅮󠄠󠅷󠅡󠅳󠄠󠅣󠅡󠅬󠅬󠅥󠅤󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅰󠅵󠅢󠅬󠅩󠅣󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅳󠅨󠅯󠅷󠄠󠅯󠅮󠅬󠅹󠄠󠅰󠅵󠅢󠅬󠅩󠅣󠄠󠅡󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅳󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅡󠅬󠅬󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅩󠅮󠅣󠅬󠅵󠅤󠅥󠄠󠅡󠅬󠅬󠄠󠅩󠅮󠅦󠅯󠅲󠅭󠅡󠅴󠅩󠅯󠅮󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅲󠅥󠅴󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅴󠅨󠅥󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅥󠅤󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅯󠅢󠅪󠅥󠅣󠅴󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅳󠅴󠅲󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅴󠅨󠅥󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠄠󠅳󠅴󠅲󠅩󠅮󠅧󠄠󠅩󠅮󠅳󠅴󠅥󠅡󠅤󠄠󠅯󠅦󠄠󠅰󠅲󠅩󠅮󠅴󠅩󠅮󠅧󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅧󠅲󠅡󠅹󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅤󠅩󠅳󠅡󠅢󠅬󠅥󠄠󠅣󠅯󠅬󠅯󠅲󠅦󠅵󠅬󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠄠󠅩󠅮󠄠󠅴󠅨󠅥󠄠󠅣󠅯󠅮󠅳󠅯󠅬󠅥󠅜󠅮󠄠󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅓󠅔󠅒󠅽󠄮󠅣󠅯󠅬󠅯󠅲󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅥󠅮󠅦󠅯󠅲󠅣󠅥󠄠󠅣󠅯󠅬󠅯󠅲󠅦󠅵󠅬󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠅳󠄠󠅩󠅮󠄠󠅴󠅨󠅥󠄠󠅣󠅯󠅮󠅳󠅯󠅬󠅥󠅜󠅮󠅃󠅡󠅬󠅬󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅷󠅡󠅴󠄮󠅬󠅯󠅣󠅡󠅬󠅳󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅯󠅲󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅷󠅡󠅴󠄨󠄩󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄠󠅬󠅯󠅣󠅡󠅬󠄠󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄮󠅜󠅮󠅃󠅡󠅬󠅬󠄠󠅻󠅳󠅴󠅹󠅬󠅥󠄮󠅃󠅏󠅄󠅅󠅽󠅷󠅡󠅴󠄮󠅧󠅬󠅯󠅢󠅡󠅬󠅳󠅻󠅒󠅅󠅓󠅅󠅔󠅽󠄠󠅴󠅯󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄠󠅧󠅬󠅯󠅢󠅡󠅬󠄠󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄮󠄧󠄊󠄉󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅬󠅯󠅲󠅟󠅥󠅮󠅡󠅢󠅬󠅥󠅤󠄨󠄩󠄺󠄊󠄉󠄉󠄉󠅴󠅥󠅸󠅴󠄽󠅟󠅳󠅴󠅲󠅩󠅰󠅟󠅣󠅯󠅬󠅯󠅲󠄨󠅴󠅥󠅸󠅴󠄩󠄊󠄉󠄉󠅰󠅲󠅩󠅮󠅴󠄨󠅴󠅥󠅸󠅴󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅣󠅡󠅬󠅬󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠄪󠅡󠅲󠅧󠅳󠄬󠄠󠄪󠄪󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅡󠅲󠅧󠅳󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅣󠅯󠅰󠅹󠄨󠄪󠄪󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠄪󠅡󠅲󠅧󠅳󠄩󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅫󠅷󠅡󠅲󠅧󠅳󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅣󠅯󠅰󠅹󠄨󠄪󠄪󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄊󠄉󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠄉󠅦󠅲󠅡󠅭󠅥󠄽󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅳󠅴󠅡󠅣󠅫󠅟󠅦󠅲󠅡󠅭󠅥󠄨󠄲󠄩󠄊󠄉󠄉󠄉󠅬󠅯󠅣󠅡󠅬󠅟󠅶󠅡󠅲󠅳󠄽󠅦󠅲󠅡󠅭󠅥󠄮󠅦󠅟󠅬󠅯󠅣󠅡󠅬󠅳󠄠󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠄠󠅥󠅬󠅳󠅥󠄠󠅻󠅽󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅰󠅲󠅩󠅮󠅴󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄨󠅬󠅯󠅣󠅡󠅬󠅟󠅶󠅡󠅲󠅳󠄬󠄠󠄧󠅌󠅯󠅣󠅡󠅬󠄠󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄧󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅷󠅡󠅴󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅩󠅮󠅟󠅰󠅲󠅯󠅧󠅲󠅥󠅳󠅳󠄽󠅔󠅲󠅵󠅥󠄊󠄉󠄉󠅴󠅲󠅹󠄺󠄊󠄉󠄉󠄉󠅯󠅵󠅴󠅰󠅵󠅴󠄽󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅦󠅯󠅲󠅭󠅡󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄬󠄠󠄪󠄪󠅳󠅥󠅬󠅦󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄊󠄉󠄉󠄉󠅯󠅵󠅴󠅰󠅵󠅴󠅟󠅲󠅥󠅴󠅵󠅲󠅮󠄽󠅳󠅥󠅬󠅦󠄮󠅟󠅤󠅩󠅳󠅰󠅬󠅡󠅹󠅟󠅯󠅵󠅴󠅰󠅵󠅴󠄨󠅯󠅵󠅴󠅰󠅵󠅴󠄩󠄊󠄉󠄉󠄉󠅩󠅦󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠅟󠅲󠅥󠅴󠅵󠅲󠅮󠄺󠄊󠄉󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠅟󠅲󠅥󠅴󠅵󠅲󠅮󠄊󠄉󠄉󠄉󠅩󠅦󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅧󠅥󠅴󠄨󠄧󠅲󠅥󠅴󠄧󠄬󠄠󠅆󠅡󠅬󠅳󠅥󠄩󠄺󠄊󠄉󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅯󠅴󠅨󠅥󠅲󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅎󠅯󠅮󠅥󠄊󠄉󠄉󠅦󠅩󠅮󠅡󠅬󠅬󠅹󠄺󠄊󠄉󠄉󠄉󠅷󠅡󠅴󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅩󠅮󠅟󠅰󠅲󠅯󠅧󠅲󠅥󠅳󠅳󠄽󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠅤󠅥󠅦󠄠󠅣󠅯󠅰󠅹󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠄪󠄪󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄺󠄊󠄉󠄉󠅮󠅥󠅷󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄽󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅣󠅯󠅰󠅹󠄨󠄩󠄊󠄉󠄉󠅦󠅯󠅲󠄠󠅮󠅡󠅭󠅥󠄠󠅩󠅮󠄠󠅫󠅷󠅡󠅲󠅧󠅳󠄮󠅣󠅯󠅰󠅹󠄨󠄩󠄺󠄊󠄉󠄉󠄉󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠅩󠅮󠄠󠅻󠄧󠅲󠅥󠅴󠄧󠄬󠄠󠄧󠅳󠅴󠅲󠄧󠄬󠄠󠄧󠅧󠅲󠅡󠅹󠄧󠄬󠄠󠄧󠅣󠅯󠅬󠅯󠅲󠄧󠅽󠄺󠄊󠄉󠄉󠄉󠄉󠅮󠅥󠅷󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠅛󠅮󠅡󠅭󠅥󠅝󠄽󠅫󠅷󠅡󠅲󠅧󠅳󠄮󠅰󠅯󠅰󠄨󠅮󠅡󠅭󠅥󠄩󠄊󠄉󠄉󠅮󠅥󠅷󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄽󠅳󠅥󠅬󠅦󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄮󠅣󠅯󠅰󠅹󠄨󠄩󠄊󠄉󠄉󠅮󠅥󠅷󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄮󠅵󠅰󠅤󠅡󠅴󠅥󠄨󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄊󠄉󠄉󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄽󠅗󠅡󠅴󠄨󠄪󠄪󠅮󠅥󠅷󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄩󠄊󠄉󠄉󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄽󠅮󠅥󠅷󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅤󠅩󠅳󠅰󠅬󠅡󠅹󠅟󠅯󠅵󠅴󠅰󠅵󠅴󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅮󠅯󠅴󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅬󠅯󠅲󠅟󠅥󠅮󠅡󠅢󠅬󠅥󠅤󠄨󠄩󠄺󠄊󠄉󠄉󠄉󠅯󠅵󠅴󠅰󠅵󠅴󠄽󠅟󠅳󠅴󠅲󠅩󠅰󠅟󠅣󠅯󠅬󠅯󠅲󠄨󠅯󠅵󠅴󠅰󠅵󠅴󠄩󠄊󠄉󠄉󠅩󠅦󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅧󠅥󠅴󠄨󠄧󠅳󠅴󠅲󠄧󠄬󠄠󠅆󠅡󠅬󠅳󠅥󠄩󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅯󠅵󠅴󠅰󠅵󠅴󠄊󠄉󠄉󠅰󠅲󠅩󠅮󠅴󠄨󠅯󠅵󠅴󠅰󠅵󠅴󠄩󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅎󠅯󠅮󠅥󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅣󠅯󠅬󠅯󠅲󠅟󠅥󠅮󠅡󠅢󠅬󠅥󠅤󠄨󠅳󠅥󠅬󠅦󠄩󠄺󠄊󠄉󠄉󠅩󠅦󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅧󠅥󠅴󠄨󠄧󠅣󠅯󠅬󠅯󠅲󠄧󠄬󠄠󠅆󠅡󠅬󠅳󠅥󠄩󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅔󠅲󠅵󠅥󠄊󠄉󠄉󠅩󠅦󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠄮󠅧󠅥󠅴󠄨󠄧󠅧󠅲󠅡󠅹󠄧󠄬󠄠󠅆󠅡󠅬󠅳󠅥󠄩󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅆󠅡󠅬󠅳󠅥󠄊󠄉󠄉󠅥󠅮󠅶󠅟󠅣󠅯󠅬󠅯󠅲󠄽󠅻󠄧󠅦󠅡󠅬󠅳󠅥󠄧󠄺󠄠󠅆󠅡󠅬󠅳󠅥󠄬󠄠󠄧󠅴󠅲󠅵󠅥󠄧󠄺󠄠󠅔󠅲󠅵󠅥󠅽󠄮󠅧󠅥󠅴󠄨󠅯󠅳󠄮󠅥󠅮󠅶󠅩󠅲󠅯󠅮󠄮󠅧󠅥󠅴󠄨󠄧󠅗󠅁󠅔󠅟󠅃󠅏󠅌󠅏󠅒󠄧󠄬󠄠󠄧󠄧󠄩󠄮󠅬󠅯󠅷󠅥󠅲󠄨󠄩󠄩󠄊󠄉󠄉󠅩󠅦󠄠󠅥󠅮󠅶󠅟󠅣󠅯󠅬󠅯󠅲󠄠󠅩󠅳󠄠󠅮󠅯󠅴󠄠󠅎󠅯󠅮󠅥󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅥󠅮󠅶󠅟󠅣󠅯󠅬󠅯󠅲󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅹󠅳󠄮󠅳󠅴󠅤󠅯󠅵󠅴󠄮󠅩󠅳󠅡󠅴󠅴󠅹󠄨󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅰󠅲󠅩󠅮󠅴󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄬󠄠󠅴󠅩󠅴󠅬󠅥󠄩󠄺󠄊󠄉󠄉󠅬󠅯󠅮󠅧󠄽󠅳󠅥󠅬󠅦󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠄮󠅧󠅥󠅴󠄨󠄧󠅬󠅯󠅮󠅧󠄧󠄬󠄠󠅆󠅡󠅬󠅳󠅥󠄩󠄊󠄉󠄉󠅬󠅩󠅮󠅥󠅳󠄽󠅬󠅩󠅳󠅴󠄨󠅟󠅲󠅥󠅮󠅤󠅥󠅲󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄨󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄬󠄠󠅴󠅩󠅴󠅬󠅥󠄬󠄠󠅬󠅯󠅮󠅧󠄩󠄩󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅤󠅩󠅳󠅰󠅬󠅡󠅹󠅟󠅯󠅵󠅴󠅰󠅵󠅴󠄨󠄧󠅜󠅮󠄧󠄮󠅪󠅯󠅩󠅮󠄨󠅬󠅩󠅮󠅥󠅳󠄩󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅴󠅲󠅵󠅥󠅤󠅩󠅶󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅡󠅤󠅤󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅬󠅳󠅨󠅩󠅦󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅲󠅳󠅨󠅩󠅦󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅯󠅲󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅲󠅯󠅲󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅬󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅯󠅴󠅨󠅥󠅲󠄩󠄺󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠄨󠅯󠅴󠅨󠅥󠅲󠄩󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅧󠅥󠅴󠅡󠅴󠅴󠅲󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅮󠅡󠅭󠅥󠄩󠄺󠄊󠄉󠄉󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄽󠅳󠅥󠅬󠅦󠄮󠅣󠅯󠅰󠅹󠄨󠄩󠄊󠄉󠄉󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠅩󠅮󠄠󠅻󠄧󠅳󠅨󠅯󠅲󠅴󠄧󠄬󠄠󠄧󠅳󠄧󠅽󠄺󠄊󠄉󠄉󠄉󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠅛󠄧󠅳󠅨󠅯󠅲󠅴󠄧󠅝󠄽󠅔󠅲󠅵󠅥󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠅩󠅮󠄠󠅻󠄧󠅬󠅯󠅮󠅧󠄧󠄬󠄠󠄧󠅤󠅵󠅮󠅤󠅥󠅲󠄧󠄬󠄠󠄧󠅣󠅯󠅤󠅥󠄧󠄬󠄠󠄧󠅮󠅯󠅤󠅯󠅣󠅳󠄧󠄬󠄠󠄧󠅣󠅡󠅬󠅬󠅥󠅲󠄧󠄬󠄠󠄧󠅰󠅵󠅢󠅬󠅩󠅣󠄧󠄬󠄠󠄧󠅡󠅬󠅬󠄧󠅽󠄺󠄊󠄉󠄉󠄉󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄮󠅟󠅩󠅮󠅳󠅰󠅥󠅣󠅴󠅟󠅫󠅷󠅡󠅲󠅧󠅳󠅛󠅮󠅡󠅭󠅥󠅝󠄽󠅔󠅲󠅵󠅥󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠅩󠅮󠄠󠅻󠄧󠅲󠅥󠅴󠄧󠄬󠄠󠄧󠅳󠅴󠅲󠄧󠄬󠄠󠄧󠅧󠅲󠅡󠅹󠄧󠄬󠄠󠄧󠅣󠅯󠅬󠅯󠅲󠄧󠅽󠄺󠄊󠄉󠄉󠄉󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄮󠅟󠅣󠅯󠅮󠅦󠅩󠅧󠅛󠅮󠅡󠅭󠅥󠅝󠄽󠅔󠅲󠅵󠅥󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠄽󠄽󠄠󠄧󠅬󠅯󠅣󠅡󠅬󠅳󠄧󠄺󠄊󠄉󠄉󠄉󠅦󠅲󠅡󠅭󠅥󠄽󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅳󠅴󠅡󠅣󠅫󠅟󠅦󠅲󠅡󠅭󠅥󠄨󠄲󠄩󠄊󠄉󠄉󠄉󠅬󠅯󠅣󠅡󠅬󠅟󠅶󠅡󠅲󠅳󠄽󠅦󠅲󠅡󠅭󠅥󠄮󠅦󠅟󠅬󠅯󠅣󠅡󠅬󠅳󠄠󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠄠󠅥󠅬󠅳󠅥󠄠󠅻󠅽󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅰󠅲󠅩󠅮󠅴󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄨󠅬󠅯󠅣󠅡󠅬󠅟󠅶󠅡󠅲󠅳󠄬󠄠󠄧󠅌󠅯󠅣󠅡󠅬󠄠󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄧󠄩󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠄽󠄽󠄠󠄧󠅧󠅬󠅯󠅢󠅡󠅬󠅳󠄧󠄺󠄊󠄉󠄉󠄉󠅦󠅲󠅡󠅭󠅥󠄽󠅟󠅣󠅡󠅬󠅬󠅥󠅲󠅟󠅳󠅴󠅡󠅣󠅫󠅟󠅦󠅲󠅡󠅭󠅥󠄨󠄲󠄩󠄊󠄉󠄉󠄉󠅧󠅬󠅯󠅢󠅡󠅬󠅟󠅶󠅡󠅲󠅳󠄽󠅦󠅲󠅡󠅭󠅥󠄮󠅦󠅟󠅧󠅬󠅯󠅢󠅡󠅬󠅳󠄠󠅩󠅦󠄠󠅦󠅲󠅡󠅭󠅥󠄠󠅥󠅬󠅳󠅥󠄠󠅻󠅽󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄮󠅟󠅰󠅲󠅩󠅮󠅴󠅟󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄨󠅧󠅬󠅯󠅢󠅡󠅬󠅟󠅶󠅡󠅲󠅳󠄬󠄠󠄧󠅇󠅬󠅯󠅢󠅡󠅬󠄠󠅶󠅡󠅲󠅩󠅡󠅢󠅬󠅥󠅳󠄧󠄩󠄊󠄉󠄉󠅥󠅬󠅩󠅦󠄠󠅮󠅡󠅭󠅥󠄠󠄽󠄽󠄠󠄧󠅷󠅡󠅴󠄧󠄺󠄊󠄉󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅳󠅥󠅬󠅦󠄊󠄉󠄉󠅥󠅬󠅳󠅥󠄺󠄊󠄉󠄉󠄉󠅲󠅡󠅩󠅳󠅥󠄠󠅁󠅴󠅴󠅲󠅩󠅢󠅵󠅴󠅥󠅅󠅲󠅲󠅯󠅲󠄊󠄉󠄉󠅲󠅥󠅴󠅵󠅲󠅮󠄠󠅮󠅥󠅷󠅟󠅷󠅡󠅴󠄊󠅣󠅬󠅡󠅳󠅳󠄠󠅓󠅴󠅹󠅬󠅥󠄺󠄊󠄉󠅂󠅁󠅒󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠄻󠄳󠄴󠅭󠄧󠄊󠄉󠅔󠅒󠅁󠅉󠅔󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄱󠄻󠄳󠄴󠅭󠄧󠄊󠄉󠅈󠅅󠅁󠅄󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄱󠄻󠄳󠄷󠅭󠄧󠄊󠄉󠅓󠅔󠅒󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠄻󠄳󠄲󠅭󠄧󠄊󠄉󠅎󠅕󠅍󠅂󠅅󠅒󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠄻󠄳󠄱󠅭󠄧󠄊󠄉󠅎󠅏󠅎󠅅󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠄻󠄳󠄵󠅭󠄧󠄊󠄉󠅔󠅒󠅕󠅅󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄱󠄻󠄳󠄲󠅭󠄧󠄊󠄉󠅆󠅁󠅌󠅓󠅅󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄱󠄻󠄳󠄱󠅭󠄧󠄊󠄉󠅄󠅏󠅃󠅓󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄲󠄻󠄳󠄷󠅭󠄧󠄊󠄉󠅋󠅅󠅙󠅗󠅏󠅒󠅄󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠄻󠄳󠄴󠅭󠄧󠄊󠄉󠅃󠅁󠅌󠅌󠅁󠅂󠅌󠅅󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄱󠄻󠄳󠄲󠅭󠄧󠄊󠄉󠅖󠅁󠅒󠅉󠅁󠅂󠅌󠅅󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄱󠄻󠄳󠄳󠅭󠄧󠄊󠄉󠅃󠅏󠅄󠅅󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠄻󠄳󠄳󠅭󠄧󠄊󠄉󠅤󠅥󠅦󠄠󠅟󠅟󠅩󠅮󠅩󠅴󠅟󠅟󠄨󠅳󠅥󠅬󠅦󠄩󠄺󠄊󠄉󠄉󠅦󠅯󠅲󠄠󠅣󠅨󠅵󠅮󠅫󠄠󠅩󠅮󠄠󠅦󠅩󠅬󠅴󠅥󠅲󠄨󠅢󠅯󠅯󠅬󠄬󠄠󠅯󠅳󠄮󠅥󠅮󠅶󠅩󠅲󠅯󠅮󠄮󠅧󠅥󠅴󠄨󠄧󠅗󠅁󠅔󠅟󠅃󠅏󠅌󠅏󠅒󠅓󠄧󠄬󠄠󠄧󠄧󠄩󠄮󠅳󠅰󠅬󠅩󠅴󠄨󠄧󠄬󠄧󠄩󠄩󠄺󠄊󠄉󠄉󠄉󠅮󠅡󠅭󠅥󠄬󠄠󠅣󠅯󠅤󠅥󠄽󠅣󠅨󠅵󠅮󠅫󠄮󠅳󠅴󠅲󠅩󠅰󠄨󠄩󠄮󠅳󠅰󠅬󠅩󠅴󠄨󠄧󠄽󠄧󠄩󠄊󠄉󠄉󠄉󠅳󠅥󠅴󠅡󠅴󠅴󠅲󠄨󠅳󠅥󠅬󠅦󠄬󠄠󠅮󠅡󠅭󠅥󠄮󠅵󠅰󠅰󠅥󠅲󠄨󠄩󠄬󠄠󠅦󠄧󠅜󠅸󠄱󠅢󠅛󠅻󠅣󠅯󠅤󠅥󠅽󠅭󠄧󠄩󠄊󠅒󠅅󠅓󠅅󠅔󠄽󠄧󠅜󠅸󠄱󠅢󠅛󠄰󠅭󠄧󠄊󠅳󠅴󠅹󠅬󠅥󠄽󠅓󠅴󠅹󠅬󠅥󠄨󠄩󠄊󠅷󠅡󠅴󠄽󠅗󠅡󠅴󠄨󠄩'))
```
to unlock the superpowers
```python
wat('WAT is going on?')
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
List the attributes and their types to see what's really inside the inspected object.
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
export WAT_COLORS="BAR=0;34,TRAIT=1;34,HEAD=1;37,STR=0;32,NUMBER=0;31,NONE=0;35,TRUE=1;32,FALSE=1;31,DOCS=2;37,KEYWORD=0;34,CALLABLE=1;32,VARIABLE=1;33,CODE=0;33"
```

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
