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
glyph = '🙀󠅸󠆜󠇕󠅛󠇫󠅮󠇜󠇆󠄕ⷾ󠇯󠆧󠄠󠇔󠄟󠄤󠆝󠇍󠇖󠅎󠅺󠄁󠆔󠇐󠆭󠅬󠅯󠅒󠆣󠆎󠅕󠇈󠅊󠆂󠅂󠄒󠄈󠇮󠅲󠅖󠅢󠇄󠄥󠄗󠄤󠇗󠇒󠅶󠆱󠅀󠄞󠆢󠇏󠇐󠄇󠇋󠆓ⷴ󠅜󠇦󠅎󠅲󠄥󠇇󠄅󠇚󠄊󠆰󠅄󠇎󠇌ⷹ󠇦󠇌󠄹󠅧󠇎󠅥󠆆󠅞󠄶ⷵ󠄪󠇈󠆳󠄮󠅛󠆔󠅙󠇛󠆊󠄶󠄨󠅖󠇫󠆺󠇩󠅌󠇓󠄓󠇙󠅐󠅔󠇭󠅚󠄬󠄺ⷵ󠅚󠇫󠆎󠅆󠆨󠆧󠅶󠇛󠄾󠅙󠄢󠅞󠆷󠅝󠄗󠇕󠆵󠆂󠄺󠆩󠆶󠆓󠇠󠅴󠇝󠄕󠅵󠆕󠆕󠆓󠇠󠅼󠆻󠄖󠅏ⷾ󠅬ⷰ󠇩󠅷ⷰ󠆆󠇡󠅟󠇕󠇕󠆲󠆸󠄾󠅾󠄒󠇀󠅏󠅻󠄃󠇔󠇇󠇁󠆼󠆮󠅋󠅺󠇏󠄷󠅕󠄮󠄚󠆫󠆡󠆪ⷳ󠅺󠇑󠅚󠄍󠅥󠅝󠅝󠅛󠆯󠆋󠄺󠄗ⷶ󠅫󠅖󠆖󠄎ⷽ󠆺󠄩󠄾󠅤󠆝󠄚󠄲󠇆󠇒󠅉󠇗󠄵󠇅󠅼󠄃󠇣󠅸󠇒󠅬󠄅󠄔󠅭󠇗󠇐󠇛󠆇󠆬󠇜󠇀󠄫󠄬󠆑󠅞󠅡󠇡ⷰ󠅆󠄫󠅔󠄳󠅦ⷳ󠅒󠄜󠅚󠆄󠇋󠄄󠆭󠆻󠆸󠆮󠆲󠅮󠇓󠅀󠆛󠆒󠇚󠄅󠇌󠅷󠇅ⷴⷵ󠇂󠅯󠇎󠇅󠅒󠅩󠄧󠅝󠇖󠇍󠄪󠇫󠆢󠅺ⷾ󠇓󠄤󠅸󠄺󠅡󠄑󠄦󠇟󠅤󠅥󠄫󠄦󠅲󠅪ⷵ󠇆󠇂󠅓󠅯󠄨󠄹ⷵ󠆌󠅢󠇓󠇏󠄤󠄳ⷵ󠆶󠇞󠇌󠇋󠅢󠆡󠇞󠆠󠆋󠄟󠇣󠅣󠄩󠅮󠇔󠅝󠇢󠅨󠄲󠅢󠄎󠇨󠆷󠇦󠆀﻿󠄄󠅵󠆃󠄐󠆚󠄓ⷾ󠄣󠅙󠇁󠅟󠅺󠄀󠄱󠆄󠆿󠅌󠄋󠆳󠇅󠅿󠅴󠆫󠄔󠄥󠄠󠅵󠆒󠇕󠆘󠄘󠆫󠄷󠇝󠅺󠇓󠄥󠅥󠇑󠅶󠅑󠆺󠄭󠅄󠆙󠆧󠅊󠅞󠅥󠅑󠆉󠆖󠇅󠇅󠇬󠇇󠅌󠅒󠄬󠇑󠆚󠆧󠅭󠆗󠄃ⷱ󠆴󠅨󠆳󠆮󠇛󠅆󠅲󠆝󠆤󠅨󠇑󠆬󠄊󠇐󠅀󠅺󠅗󠇤󠇝󠅍󠅒󠆷󠇓󠅫󠇑󠆥󠆺󠆵󠄭ⷾ󠄡󠆢󠅸󠆺󠆨󠇋󠇍󠆪󠅪󠄵󠄕󠄳󠄲󠆅󠇉󠅅󠇓󠅅󠇏󠅀󠄿󠇝󠆶󠄔󠇓󠆗󠄧󠅧󠇁󠅧󠅁ⷸ󠇋󠄿󠅿󠄎󠆃󠆧󠄞󠄴󠅴󠆜󠇍󠇞󠇏󠇎󠅣󠄟󠄤󠅛󠆯󠅅󠆕󠅇󠄟󠆋󠇐󠄈󠆰󠆬󠄪󠄈󠄯󠆫󠅰ⷺ󠅓󠅝󠅔󠄑󠇃󠇅󠅤󠅅󠄏󠄊󠇧󠅘󠄉󠆇󠇟󠆧󠅲󠅋󠅩󠇞󠆈󠄾󠄠󠄟󠆐󠅞󠆋󠅊󠄴󠆠󠆎󠆔󠄇󠄁󠇪󠆲󠆎󠆘󠄉󠄰󠇛󠆔󠅶󠅎󠄢󠄍󠆖󠇟󠅸󠄪󠇒﻿󠅹󠆳󠄑󠆊󠇡󠆵󠄚󠆌󠆏󠄸󠅆󠆫󠇈ⷴ󠄅󠅉󠆂󠆨󠇔󠆋ⷶ󠇠ⷶ󠆤󠇐󠅕󠆬󠅓󠅐󠅇󠇝󠅄󠅺ⷲ󠆸󠇇󠅷󠆸󠅣󠅱󠆞󠆟󠆝󠆼󠄹󠇟ⷳ󠇞󠇞󠆑ⷰⷶ󠇁󠅎󠇓󠇭󠅃󠆢󠄓󠅠ⷹ󠄏󠄠󠄀󠇉󠄸ⷽ󠄨󠄕ⷲ󠅮󠆓󠅡󠇏󠅟󠅦󠄧󠆯ⷷ󠄻󠆳󠆪󠆽󠇬󠄏󠆵󠄼󠇑ⷵ󠅨󠅱󠇢󠅋󠅄󠆿󠅐󠄠󠄬󠆯󠇁󠆹󠇈󠅡󠄹󠄬󠅢󠆋󠆄󠅝󠅧󠆍󠆨󠆺󠄶󠄉󠄧󠆁󠄴󠆖󠄔󠆭󠆜󠆛󠅩󠅠󠅫󠅍󠆢󠆵󠄢󠇉󠄞󠆐󠆍󠄚󠆥󠄧󠆗󠄍󠅲󠅮󠆴󠄱󠇩󠄽󠄣󠆘󠄔ⷶ󠅟󠇃󠇦󠄑󠆦󠅩󠄩󠆪󠄴󠄅󠆦󠇞󠇕󠆕󠆈󠇭󠅍󠇙󠅬󠇍󠇋󠇨󠇄󠅀󠅭󠄦󠅵󠇭󠄏󠆺󠅸󠄭󠆖󠆊󠇄ⷽ󠅂󠆬󠄻ⷲ󠇩󠆳󠆦󠆩󠄛󠅷󠆆󠄵󠆆󠄋󠆟󠅟󠆄󠄰󠇃󠄰󠅠󠄤ⷾ󠄒󠆰󠆑󠇖󠄐ⷾⷲⷳ󠆿󠅂󠆳󠆹󠆵󠇯󠅏󠅈󠇔󠄊󠄲󠇕󠇭󠄑󠅒󠅎󠄂󠆽󠄋󠇆󠅭󠅏󠅇󠄑󠆣󠅞󠇕󠄤󠆗󠄇ⷾ󠆖󠆧󠆁󠆇󠇁󠆽󠄇󠆋󠆂󠆮󠄠󠆫ⷲ󠄠󠅂󠆧󠄪󠅷󠄽󠅻󠇪󠆘󠇚󠅇󠄖󠇍󠆔󠇠󠄀󠄷󠅕󠄗󠆡󠆳󠆉󠅱󠄟󠄾󠄻󠆨󠆞󠇗󠆧󠆯󠇞󠇯󠆏󠆎󠆎󠅶󠅀󠅉󠅿󠅭󠄓󠇯󠇯󠄸󠄋󠄁ⷽ󠇍󠅅󠄏󠄇󠆤󠄋󠅈󠄓󠆘󠇀󠄂󠆻ⷲ󠄽󠄘󠆆󠄕󠅚󠆠ⷴ󠅺󠇠󠇬󠄩ⷼ󠅫󠅗󠇢󠆬󠇐󠅚󠅢󠅛󠅯󠆚󠆅󠇔󠄓󠄿󠆧󠄈󠄖󠄹󠆪󠇁󠄸󠅂󠅽󠆏󠄰󠅌󠄞󠇈󠅙󠆋󠅤ⷷ󠆲󠇚󠅱󠆫󠇙󠄕󠆖󠄞󠄸󠅁󠇒󠇀󠆙󠅊󠅔󠇚󠆤󠆅󠄎󠆑󠅇󠅩󠄁󠆡󠄠󠄵󠇭󠆎󠄯󠆟󠄄󠆷󠅢󠆛󠆔󠇙󠅪󠆞󠅧󠅄󠅻󠅌󠆿󠆧󠅨󠅠󠄽󠇛󠄢󠆏󠄎ⷻ󠄳󠆗󠅸󠅭󠇚󠆂󠆬󠄠󠄉󠅩󠄣󠄃󠆯󠆡󠄹󠆘󠄜󠆚󠆜󠆹󠆆󠇍󠆇󠅌󠅀ⷶ󠄒󠇤󠅅󠇣󠆙󠆐󠅌󠄖󠆠󠄟󠇂󠅰󠇖󠅴󠇭󠅝󠇑󠇝󠅄󠆰󠅷󠅂󠆶󠄼󠇬󠄀󠆆󠆬󠅦󠇇ⷺ󠄸󠇇ⷰ󠅍󠆗󠆛󠅣󠅗󠄛󠇐󠇗󠄕󠇕󠅆󠇨󠅆󠆕󠅈ⷴ󠇦󠆖󠅓󠄓󠆢󠆄󠄚ⷷ󠄾󠄜󠆴󠆜󠆝󠄏󠆀󠆱󠇯󠅙󠅞󠅦󠆭󠆘󠇑󠄣󠆈󠄳󠇈󠇚󠅀󠄌󠇁󠄘󠇦󠆴󠅓󠅈󠆴󠅥󠅲󠄸ⷻ󠄈󠄧󠄂󠅼󠅌󠄘󠄸󠅆󠅡󠇩󠄡󠆴󠇅󠇈󠆯󠄚󠄵󠇘󠅎󠆂󠅈󠆤󠆛󠆐󠄒󠇅󠇧󠄇󠅁󠇘󠆊ⷼ󠆄󠆚󠅼󠅙󠅢󠅸󠅉󠄤󠄼󠆅󠄲󠄊󠄬󠇌󠇢󠅄󠇯󠇁󠅄󠅏󠇢󠄥󠆓󠄦ⷹ󠆓󠅿󠄧󠆖󠄔ⷴ󠄓󠄹󠆄󠄄ⷾ󠅉󠄋󠅽󠇐󠇅󠆲󠄦󠄜󠇍󠆦󠄖󠄮󠆨󠅕󠅹󠄍󠅃󠅭󠄢󠆮󠅔󠅰ⷴ󠄃󠆮󠆂󠆂󠇇󠇄󠇄󠆑󠅸󠄐󠄲󠆌󠄠󠄞󠇄󠅺󠆳󠄏ⷹ󠆤󠅣󠇋󠅌󠇅󠆲󠆸󠅏󠅂󠄮󠅗󠅔󠅖󠇢󠆒󠇕󠄍󠄤󠅸󠆐󠇇󠄭󠄷󠄕󠇭󠇗󠄑󠆈󠆬󠇝󠅖󠆋󠄀󠆅󠄲󠄈󠇣󠅐󠆣󠅓󠄴󠅝󠄫󠇑󠇝󠇔ⷹ󠅀󠇇󠅼󠅓󠆔󠅝󠅡󠅈󠅮󠆲󠅶󠄨󠄄󠄎󠄰󠅣󠆳󠅡󠅻󠅼󠇕󠄟󠇚󠆙󠆬󠅶󠆢󠅿󠆝ⷽⷽ󠇇󠇓󠄳󠇈󠆒󠅸󠇘󠅞󠄶󠆿󠄺󠅹ⷻⷶ󠇤󠇥󠇛󠇙󠅾󠆇󠄓󠆪󠇖ⷷ󠅯󠆾󠅽󠅷󠅲ⷾⷽ󠄙󠄴󠄛󠇩󠆛󠆤󠅊󠅛󠆇󠇯󠇘󠄇󠄌󠅂ⷲ󠆡󠄖󠄎󠅔󠅌󠅤󠄂󠆁󠆲󠆃󠇓ⷷ󠆾󠄑󠅌󠅠󠅏󠇤󠆐ⷵ󠅤󠄨󠅜󠄶󠄋󠇏󠄃󠇨󠅕󠄮󠆳󠆢󠄔󠅹󠇐󠇕󠄁󠇌󠄐󠇘󠆱󠄢󠇘󠇑󠅞󠄑ⷱ󠄞󠄞󠆅󠇍󠆽󠄓󠇗󠄥󠇯󠆸󠄃󠄬󠅞󠇥󠄐󠄧󠇞󠄗󠄭󠇭󠇞󠄞󠄓󠅺󠅋󠇋󠅝󠄴󠆥󠆴󠄺󠅲󠄊󠄋󠆢󠅟󠇒󠆄󠇬󠄇󠅒󠆊󠅒󠆐󠆱󠇡󠇠󠇪󠄺󠄲󠆻󠇏󠄊󠄧󠆐󠅿󠄵󠄅󠆹󠄲󠅼ⷳ󠆢󠄄󠄹󠄁󠄤ⷷ󠆪󠄅󠆊󠅖󠅣󠄞󠅩󠄠󠅜󠇒󠇩󠆀󠅞󠆓󠆅󠇪󠅱󠆨󠅻󠅢󠅝󠇓󠄻󠆳󠆓󠆴󠅩󠅲󠅼󠆊󠅝󠅣󠄌󠅔󠇆ⷾ󠇃󠇉󠇙󠄛󠆶󠄻󠄝󠅕󠆵󠅉󠆞󠆾󠆞󠇭󠆥󠇚󠄐󠅹󠄟󠄤󠇁󠅎󠇏󠆪󠄔󠇨󠅱󠇕󠆉ⷻ󠅎󠆅󠇍󠆢󠅩󠆹󠄺󠆛󠄄󠇩󠄄󠇦󠅮󠆻󠄄󠆻󠆧󠆐󠅂󠅷󠄅󠇭󠅓󠅊󠆹󠅌󠆙󠇔󠅶󠆸󠄃󠄱󠆽󠅵󠅊󠄡󠄃󠄔󠇇󠇁󠆋󠇠ⷹ󠆳󠅧󠅽󠇃󠇓󠅃󠄮󠆎󠆡﻿󠅊󠅕󠆓󠅔󠅮󠅂󠇪ⷺ󠅤󠅰󠅬󠅟󠇁󠇒󠅍󠄌󠆨󠅗󠄪󠆉󠆤󠅤󠆒󠇖ⷾ󠄆󠄀󠇉󠄚󠅉󠆺󠅮󠆒󠇚󠄏󠅤󠆪󠅎󠅞󠆪󠄆󠄿󠆐󠆜ⷶ󠇦󠄵󠅮󠄢󠆰󠄓󠇍󠇟󠇈󠅮󠅌󠅚󠄟󠆑󠆱󠄞󠆀󠄽󠇆󠅬󠇏󠇉󠅠󠆡󠅁󠅣󠅟󠅖󠅾󠅊󠇬󠆂󠄟󠄀󠆖󠄆󠇥󠅬󠄞󠅻󠇟󠅠󠇂󠄿󠄁󠄇󠆆󠆞󠄨󠅹󠅦󠇔󠅒󠆴󠇠󠄨󠆺󠆬󠅚󠇨󠇡󠆸󠄩ⷺ󠅓󠄞󠄩󠆧󠅺󠅾󠆶󠄏󠅷󠆲󠇆󠆕󠆬󠄞󠄩󠄰󠄮󠇆󠇇󠅜󠆋ⷶ󠇢󠇯󠅎󠇟󠇍ⷶ󠄸󠇄󠅙󠆪󠅍󠆏󠇜󠆎󠇓󠆟󠆟󠅽󠄿󠇛󠇣󠆐󠅑󠅺󠄺󠆲󠄚󠄇ⷸ󠇦󠇤󠇭ⷻ󠇙󠆞󠄆ⷹ󠄐󠅽󠅹󠅀ⷸ󠇯󠆠󠇀󠄨󠇫󠆬󠆋󠄇󠄄󠆣󠄗ⷵⷽ󠅷󠄯󠅧󠅧ⷻ󠇝󠅀󠇩󠄾󠄈󠆛󠄗󠆋󠆮󠄏󠆧󠄔󠆈󠆽󠅽󠄭󠄪󠄅󠇂󠇆󠅼󠄞󠆏󠅃󠇣󠄡󠇘󠄸󠄴ⷶ󠄾󠄆󠅚󠆞󠅥󠅐󠄆󠅤󠄥󠆟󠅙󠅵󠄍󠆉󠇔󠆼󠇉󠄖󠆷󠄐󠅽󠄀󠅰󠅱󠆓󠄴󠅢󠆺󠇜󠆔󠄥󠆽󠅄󠇡󠇗󠇑ⷴ󠅩ⷼ󠄢󠆜󠄨󠄄󠇍󠇩󠄀󠇩󠆸󠄼󠇉󠆁󠅾󠇝󠅷󠆴󠅽󠆌󠇩󠄵󠇤󠄿󠇫󠇨󠅹󠇬ⷸ󠇞󠄗󠆎󠄊󠅼󠅴󠄴󠅣󠅵󠅚󠇣󠆥󠄄󠅽󠄍󠇀󠆣󠄫󠄤󠅫ⷻ󠆰󠇐󠅞󠄄󠅟󠄎󠆸󠅕󠇗󠇜󠅦󠅧󠅧󠆧󠅧󠇇󠄐󠇜󠅫󠇈󠇁󠇄󠆺󠇜󠄆󠄕ⷸ󠅬󠆑ⷻ󠆦󠆂󠆮󠄍󠆽󠄸󠇌󠅺󠇀󠇜󠅨󠆍󠆻󠇝󠇞󠆳󠆴󠅎󠆬󠇚󠄤󠆂󠅑󠆮󠄧󠆸ⷵⷸ󠇇󠇈󠇤ⷹ󠄊󠅿󠅄󠇈󠆕󠄛󠆤󠇭󠅜󠆺󠄭󠆦󠄄󠄞󠇅󠅎󠇘󠅵󠇣󠄭󠆍󠆠󠄸󠅪󠆎󠆓󠆨󠄭󠅾󠅨󠄝󠅲󠄕󠄻󠆍󠇠󠇨󠇒󠅛󠄥󠆝󠅙󠄦󠇦󠅸󠄳󠄊󠆱󠄕󠅏󠅅󠆵󠄍󠄃󠅾󠇑󠇭󠄧󠆼󠆈󠄂󠅯󠄶󠆘󠄹󠆕󠆵󠅗󠅸󠄂󠅊󠆾󠅐󠇓󠅆󠆒ⷸ󠅳󠆵󠄁󠄎󠆳󠄊󠅾󠆛ⷸ󠇀󠄇󠄃󠄷󠇆󠆶󠅭󠅙󠇖󠄆󠄬󠇛󠇮󠆿󠅠󠅙󠇥󠆐󠅻󠅰󠆗󠅹󠅱󠄵󠅤󠅗󠆽ⷰ󠇢󠄱󠅏󠇒󠆆󠅦󠄔󠄷󠅎ⷲ󠆟󠆷󠆔󠆋󠇃󠆆󠅲ⷵ󠄿󠅣󠄧󠄗󠆏󠄷󠆓󠆫󠅁󠄫󠇑󠇇󠆻󠆩󠇔󠇕󠆪󠇎󠄷󠄥󠇗󠇌󠇩󠄴󠅍ⷹ󠄵󠅍󠆕󠆌ⷹ󠅝󠄅󠅟󠅌󠄅󠅥󠄋󠆟󠆚󠄃󠄅󠆕󠆐󠆩󠅍ⷻ󠆐󠅻󠅑󠅳󠅱󠄙󠆷󠄿󠇨󠅑󠆙󠆂󠆑ⷷ󠇓󠅑󠅒󠅝󠆷ⷴ󠅎󠆘󠅓󠅣ⷻ󠆪󠆌󠆤󠅦󠄪󠄤󠅗󠅍󠇭󠇖󠆑󠆤󠄯󠆐󠇥ⷽ󠄤󠆘󠅧󠆭󠄠󠄜󠇔󠆞󠆨󠄶󠄫󠆺󠆒󠆈󠆴󠆠󠆐󠇔󠄻󠄍󠆒ⷻ󠇫󠆞󠅲󠅂󠆔󠆕󠆅󠇑󠇢󠆩󠄀󠅔󠅎󠄮󠄅ⷾⷴ󠇎󠆐ⷰ󠆇󠆏󠄽󠄜󠆭󠅩󠄰󠅽󠄄󠄱󠅴󠅋󠄢ⷳⷼ󠄆󠇏󠅇󠅔󠄏󠇄ⷱ󠇅󠅭󠅊󠅭󠇑󠄟ⷴⷶ󠆡󠅷󠅫󠇩ⷸ󠆊󠄘󠅶󠆍󠆧󠄛󠄣󠅺󠅲󠇎󠇉󠅴󠇟󠅴󠄉ⷵ󠅥󠇥󠆀󠆙󠄥󠅸󠄧󠆕ⷲ󠇞󠄍󠄩󠆎󠄃󠅇󠇇󠅽󠆸ⷽ󠆱󠇕󠆈󠇦󠅞󠇕ⷽ󠄼󠇙󠅡󠄄󠆋󠇚󠄔󠇥󠄉󠄥󠆍󠅿󠅐󠆗󠄋󠅫󠇏󠄎󠆓󠇄󠅎󠅙ⷺ󠆘󠅵󠆈ⷻ󠄵󠆔󠅈󠄭󠇔󠅍󠇦󠆬󠄜󠄑󠆕󠅉󠆎󠆟󠅻󠆶󠅞󠄭󠇃󠆷󠆎󠄼󠄲󠆹󠇈󠇈󠄒󠄳󠄴󠄽󠅪󠇑󠆥󠇎󠅔󠄞󠅒󠆙󠅺󠄥󠅓󠄧󠆓󠅼󠄾󠄭ⷻ󠄏󠄁󠅩󠄐󠅹󠄯󠆼󠄱󠄼󠆎󠄑ⷰ󠄘󠅽󠄂󠅮󠄳󠄻󠅼󠆅󠄷󠆴ⷰ󠄨ⷼ󠄛󠇑󠅙󠇇󠇍󠇡󠇄󠇁󠄲󠇇󠇀󠅲󠄢󠅙󠆌󠇙󠆋󠅶󠄖ⷸ󠅑󠆓󠄫󠄐󠅧󠅶󠄛󠅭󠅬󠅺󠇫󠅄󠇘󠄖󠇖󠇇󠅌ⷾ󠅚󠅂󠇘󠅳󠇛󠅘󠇞󠄁ⷸ󠄠󠄈󠄔󠇨󠅸󠅺󠄹󠅤󠄽󠇪󠄤󠇤󠆠󠇩󠆨ⷳ󠇊󠄫󠅃󠇂󠆵ⷵ󠆨󠇚󠅝󠄊󠅞󠆥󠄼󠅃ⷳ󠅶󠄅󠇟󠄲󠄒󠆇ⷻ󠅣󠅧󠆓󠄒󠄮󠅀󠄪󠅨󠅢󠇓󠄗󠇝󠄣󠅎󠅴󠇬󠆊󠆝󠄰󠅈󠄟ⷶ󠄪󠅼󠇐󠅰󠆄󠆁󠆑󠇡󠄏󠄞󠄺󠆰󠅪󠄆󠅼󠅪󠄮󠇖󠇝󠆍󠇣󠅹󠆕󠄋󠅝󠅬󠄚󠆌󠅇󠄼󠄬󠇖󠇬󠆤󠇈󠅋󠄃󠅅󠆇󠅋󠅫ⷻ󠄳󠆌󠄘󠆨󠄶󠆷󠇦󠄵󠄳󠇐󠇯󠇩󠄲󠆝󠄃󠄛󠅎󠇤󠇄󠅶󠇇󠆈󠆔󠄸󠇛󠅈󠄿󠅍󠄂󠅩󠅋󠇖󠇩󠇞󠅇󠄩󠆴󠄢󠄎󠆫󠅀󠇞󠄖󠅩󠇠󠇩󠆭󠇘󠅢󠄲󠄿󠅸󠅘󠇦󠆥󠅹󠆒󠇤󠄂󠆱󠆮󠄤󠄫󠆚󠅬ⷸ󠇨󠅌󠆞󠇬󠄻󠆔󠅱﻿󠄶󠅳󠇠󠄤󠇭󠅗󠄜󠆢󠅙󠆧󠅝󠇖󠄉󠆚󠄔󠄳󠇔󠆦󠇭󠅦󠄞󠆅󠆗󠆗ⷷ󠇏󠇧󠆗󠆗󠄗󠆗󠆗ⷹ󠅧󠇑󠅗ⷸ󠄻ⷾ󠇓󠄊󠆓󠅏ⷸ󠅇󠅔ⷲ󠆋󠆠󠄟󠄳󠄙󠆐󠆎󠆎󠆎󠇤󠅥󠄆󠄟󠅹󠅓󠆉󠆍󠅧󠆳󠇢󠄾󠅛󠅁󠆌󠄋󠄶󠇕󠅭󠅕󠇟󠅕󠄲󠅝󠅨󠅡󠄼󠅻󠅩󠇤󠄉󠅢󠅼󠇑󠆥󠅩󠇔󠆊󠅲󠄹󠄉󠆞󠄾󠅕󠆟󠅛󠇜󠇞󠅥󠇍󠆵󠅽󠅘󠆅󠄃󠆦󠆩󠇛󠆝󠆸󠆯󠇞󠅘ⷹ󠄉󠇎󠅮󠄿󠆂󠅑󠅔󠇩󠆺󠆩󠆯󠄱󠇚ⷱ󠆧󠄻󠄖󠅗ⷴ󠅱󠄁󠅳󠇥󠅚󠄲󠄚ⷰ󠅝󠇖󠄍󠆢󠆸󠅆󠇍󠆓󠆁󠄷󠆆󠇤󠇭󠅆󠆔󠅶󠄌󠅖󠇟󠆝󠆄󠇖󠆌󠅘󠅣ⷷ󠄦󠅔󠄃󠆿ⷾⷱ󠇤󠄼󠄰󠅂󠅦󠅁󠆾󠆰󠇈󠆭󠅩󠄼󠄈󠅔󠅙󠆲󠄌󠇏󠆛󠆭󠆓󠆜󠇀󠄚󠆂󠇟󠅊󠄠󠄕󠇧󠄁󠇙󠄛󠄲󠆅󠄴󠆵󠅘󠄖󠄂󠅜󠆓󠄿󠄘ⷴ󠄫󠅅󠄀󠅞󠇋󠆡󠅳󠇆󠅍󠆝󠆏󠄶󠆾󠅓󠅰󠄊󠄅󠅲󠇛󠇣󠇋󠅊󠅛󠄷󠆞󠄶ⷰ󠅍󠅮󠆟󠄧󠇮󠆳󠆦󠆿󠄩󠅲󠄻ⷴ󠄅󠅦󠄛󠆑󠄟󠆕󠄾󠄱ⷶ󠇡󠄹󠅆󠅙󠄸󠄤󠄻󠅽󠅇󠆪ⷱ󠅼󠄺󠇜󠇍󠄽󠆪󠆪󠆮󠄾󠇏󠇦ⷳ󠅆󠅼󠄨󠄠󠇦󠇦󠇬󠄛󠅸ⷾ󠆼󠅞󠅀󠆆󠄭󠆯󠄳󠅼󠄰󠇌󠆨󠅺󠅠󠇖󠄽󠅆󠅐󠅃󠅘󠄈󠇔󠅍󠇓󠅄󠄮󠆆󠅮󠇠󠅱ⷳⷹ󠅰󠅼󠆴󠇫󠇋󠇆󠇡󠆀󠆜󠆜󠄂󠅤󠄎󠇥󠅗󠆎󠄽󠇞󠄨󠄜󠅘󠅠󠆠󠆐󠆻󠄀﻿󠄡󠇑󠇝󠆍󠅨󠅠󠅷󠇟󠄈󠆥󠅾󠇄󠆾󠇋󠅚ⷾ󠄌󠄭ⷷ󠇁󠄸󠄗ⷲ󠇁󠇪󠄊󠅪󠇯󠆵󠆟󠄺ⷹ󠆴󠄀󠇨󠅘󠇛󠆢󠇜󠆠󠇆󠅋󠄬󠆛󠇙󠆇󠄎󠅈󠄖󠆶󠆌󠅅󠄤󠄷󠆐󠇅󠄮󠄨󠅩󠇔󠅘󠅻󠆖󠇘󠄵󠇃󠅘ⷼ󠆝󠅘󠇀󠆷󠄑󠇤ⷳ󠅄󠆖󠆣󠇎󠅈󠆑󠇐󠇦󠄣󠅝󠄷󠇙󠇖󠆂󠇊󠆋󠆖󠄮󠆇󠇉󠄗󠄯󠄷󠆥󠄂󠄬󠄘󠄞󠄼󠅗󠅛󠆗󠆢󠅯󠄴󠄰󠇚󠅂󠄑󠄨󠆅󠅅󠄏󠆥󠇭󠇁󠆼󠅂󠆙ⷹ󠅛󠆻󠆬󠅁󠅣󠇭ⷸ󠇞󠆏󠇢󠆁󠆭󠅎󠅄󠆁󠄉󠆎󠄣󠇘󠇗󠅥󠄽󠆷󠇀󠄭󠄀󠇮󠆱󠄐󠅂󠇟󠆻󠄪󠇧󠄍󠅫󠅊󠆡󠅨󠆂󠅁󠅹󠇤󠅕󠆥󠇤󠇓ⷺ󠇡󠅌󠆏󠄡󠄭󠅘󠅭󠇬󠅡󠇑󠅀󠅍󠆤󠇁󠆀󠆁󠄁󠆧󠄗󠅨󠄰󠄡󠆃󠆖󠇁󠆛󠄊󠇢󠅭󠅑󠆯󠆷󠆑󠄦󠆜󠇊󠆕󠅅󠆄󠅨󠅽󠇐󠆀󠆗󠇆󠄼󠇦󠆱󠅐󠄇󠅮󠅊󠇆󠆫󠇟󠄯󠇜󠇒󠆎󠄔󠇄󠅹󠆳󠇊󠆧󠅘󠇑󠄦󠄍󠆣󠆛󠅈󠄫󠄪ⷺ󠅌󠇉󠅠󠅢󠆒󠄬󠆃󠄉󠅙󠇀󠅛󠇗󠄂󠅂󠄣󠅡󠄥󠄈󠄖󠅰󠄍󠄖󠅨󠇟󠆏󠆌󠄅󠅍󠆺󠅰󠄱󠇑󠇊﻿󠅮󠅄󠅾󠆮󠇪󠅿󠇒󠆋󠇠󠆨󠆽󠆡󠆬󠄠󠄞󠄀󠅈󠅹󠆁󠄉󠆏󠆇󠇭󠆷󠄮󠆳󠅭󠇊󠅽ⷺ󠆫󠅏󠆛󠄌󠆤󠇥󠅐ⷶ󠄏󠄹󠆤󠇈󠆜󠅑󠄾󠆄󠆝󠆈󠇠󠇡󠅃󠄔󠇂󠄸󠇈󠆣󠇬󠄯󠆅󠆇󠄰󠅱󠅹󠅃ⷺ󠅱󠆾󠄣󠅙󠇢󠅧󠆭󠆥󠄧󠆯󠅑󠄱󠆻󠄙󠄎󠄙󠆞󠇊󠆹󠅺󠅛󠆠󠄒󠅷󠄪󠅻󠅲󠅖󠅀󠅔󠅆󠅎󠅶󠇚󠇌󠄘󠅲󠅄󠇯󠄌󠅉󠆍󠇚󠇉ⷵ󠆇󠆰󠅷ⷱ󠄏󠆺󠅅ⷼ󠅋󠆛󠄸󠇜ⷷ󠄅󠅢󠄸󠇡󠇔󠄸󠆑ⷳ󠆬󠇫󠅵󠇤󠅾󠆛󠆅󠄣󠆽󠇬󠅰󠇈󠄸ⷼ󠄵ⷴ󠇉󠆦󠆛󠅵󠆎󠇇󠅢󠆾󠄱󠇡󠅈󠆐󠅮󠄂󠅹󠄯󠅬󠇙󠄾󠅝󠅯󠆤󠇎󠅀󠇍󠄢ⷼ󠇄󠅎󠆎󠄴󠅎󠇊󠆳󠅌󠆹󠆕󠇘󠄾󠅻󠅹󠇨󠄣󠄼󠆥󠇜󠄾󠆎󠆯ⷴ󠇍󠅽󠇐󠅎󠅙󠅁󠅃󠅶󠇪󠇘󠆽󠇧󠅲󠅽󠇨󠇞󠆷󠄒󠅔󠅮󠄺󠄌ⷷ󠅓󠇬󠄾󠄳󠅬󠄞󠄇󠇙󠅱󠆼󠇈󠄠󠆈󠆴󠆵󠄃󠄘󠅦󠆋󠇠󠆏󠆨󠄾󠄰󠆫󠇉󠄮󠅜󠅢󠅏󠅸󠄜󠇈󠆏ⷽ󠇃󠄎󠅦󠆃󠅗󠆜󠅴󠅏󠇨󠅵󠄻󠆅ⷱ󠅅󠅓󠅗󠄼󠄙󠇤󠇫󠇩󠆫󠇓󠆷󠆧󠅧󠅔󠄸󠇅󠄐󠅬󠇯󠅄󠄓󠇅󠆎󠇐ⷵ󠄄󠇣󠆅󠆱󠅤󠅌󠆏ⷴ󠄅󠄻ⷰ󠅙󠆾󠅟󠄓󠄘󠄷󠇎󠇆󠇤󠅗󠇌󠆖󠄨󠇨ⷾ󠅻󠅰󠇓󠇐󠆚󠆰󠅛󠄋󠇐󠄐󠇑󠇝󠄁﻿󠅷󠆂󠇇󠆖󠇧󠄽󠄃󠄙󠅴󠇋󠇦󠅬󠆓󠇦󠆈󠇭󠅘󠆎󠄊󠇈󠆋󠄏󠄺󠆜ⷻ󠇑󠇆󠇆󠅕󠅱󠆉󠇇󠅘󠄠󠅙󠆞󠅿󠄚󠅀󠇙󠇞󠄔󠇋󠇮󠇓󠄰󠆚﻿󠄀󠅆󠇝󠅼󠄢󠄏󠆟󠄊󠅐󠅾󠇢󠄂󠇤󠅷󠆡󠄚󠆄󠅜󠆻󠄛󠆏󠇐ⷵ󠆚󠆜󠇉󠇙󠅈󠄦󠆺󠅐󠇩󠅈ⷱ󠇅󠄏󠄦󠇚󠄧󠆻󠆖󠅽󠄡󠅉󠆮󠇜󠄴󠆄󠆒󠄷󠄃󠄫󠄭󠄿󠇤󠄚󠆑󠄃󠅖󠄮ⷰ󠄯󠄗󠅞󠇔󠅂󠆩󠄙󠄾󠅱󠅝󠆃󠅏󠇐ⷴ󠅘󠄾󠄸󠆺󠄝󠅢󠇢󠄣󠄢󠆧󠄗󠆀󠄎󠆃󠄧󠅉󠄐󠅲󠆊󠄘ⷾ󠅿󠇥󠆜ⷽ󠅥󠇈󠆲󠇣󠇗󠆮󠆃󠇉󠇝󠆅󠅈󠇈󠅏󠅘󠆉󠆅󠄊󠅋ⷹ󠇖󠆫󠅿󠅆󠇗󠄂ⷺ󠄋󠅇󠄋󠆇󠄃󠆕󠅂󠆓󠄕󠇀󠆠ⷾ󠆬󠆘󠆾󠆣󠄜󠅋󠄻ⷸ󠄠󠇯󠄽󠇖󠅮󠄌ⷲⷲ󠇤󠄬󠄉ⷱⷼ󠇯󠇢󠇙󠅗󠅟ⷾ󠅮󠇅󠆵󠄙󠅝󠄏󠇉󠇦󠇧󠆦󠄙󠄏󠅴󠅌󠇫󠄟󠅥󠄫󠄔󠆪󠄆󠇡󠄋󠇙󠇈󠆟ⷼ󠆘ⷶ󠇧󠆪ⷽⷴ󠇝󠇌󠆴ⷾ󠅞󠇏ⷷⷽ󠇌󠄀󠄫󠄌󠆺󠇁󠄷󠇍󠄊󠄂󠆿󠄎󠆓󠆭󠅟󠄘󠄮󠇤󠇧󠆯ⷽ󠆵󠆨󠄏󠅠ⷻⷸⷺ󠄣󠇘󠄾ⷻ󠇪󠇌󠇕󠄐󠅽󠆩󠇠󠆠󠇠󠄵󠇣󠅕󠅫󠇯󠅠󠇓󠆻󠆎󠅝󠇜󠅬󠆪󠅛󠇜󠇔󠇋󠆢󠇬󠄠󠄭󠇀﻿󠇬󠄈󠆎󠅳󠄬󠆅󠅸󠄯󠅳󠄈󠄈󠆎󠄅󠆴󠅏󠇂󠇘󠅋󠅟ⷸ󠄓󠅭ⷾ󠆏󠆁󠄈󠆭󠇮ⷼ󠄔󠅅󠄒󠆺󠅶󠇞󠇊󠆯ⷰ󠆍󠆯󠆅󠆜󠅷󠆍ⷹ󠄉ⷾ﻿󠄐󠅚󠄍󠅟ⷹ󠆭󠆀󠆐󠅊󠅸󠆵󠅆󠅘󠄠󠅕ⷺ󠄉󠇙󠄌󠅸󠅡󠆕󠄐󠇇﻿󠄆󠆺󠅑󠄋󠆖'
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
