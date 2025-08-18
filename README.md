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
import zlib
glyph = '🙀󠅸󠆜󠇕󠅜󠇫󠅮󠇛󠅆󠄖ⷾ󠆟󠆧󠄠󠆼󠄿󠅈󠄦󠆪󠆚󠆴󠅻󠄁󠇜󠄲󠆻󠅎󠇢󠅶󠆃󠅵󠇣󠇂󠅶󠅛󠄔󠆶󠅁󠇐󠇢󠇈󠅦󠅍󠆑󠅚󠆒󠆊󠆣󠄕󠄄ⷴ󠄡ⷶ󠄙ⷺ󠅠󠅽󠆒󠄽󠆗󠆹󠆓󠆔󠇭󠆦󠇀󠇮󠄆󠆰󠅄󠇎󠇌ⷹ󠇦󠇌󠆙󠄳󠇧󠄲󠄳󠇊󠆼󠆩󠄗󠅁󠆞󠅵󠇙󠆬󠇌󠇚󠅖󠆴󠅁󠆱󠅘󠇖󠅍󠅧󠆊󠆞󠇈󠆂󠆢󠅪󠆗󠅢󠇖󠆩󠇗󠅚󠅗󠄴󠅂󠄽󠆵󠇫ⷶ󠇉󠄜ⷱ󠆺ⷵ󠆲󠆨󠆮󠄕󠇔󠅁󠆵󠆞󠄄󠇇󠇋󠆮󠆨󠆫󠆬󠆜󠄄󠅧󠇫󠆥󠅸ⷲ󠄷󠆃󠅏󠆟󠇁󠅛󠆆󠅿󠅝󠅗ⷳ󠇢󠅺﻿󠅉󠄀﻿󠇚󠄛󠆠󠇞󠄏󠆮󠇪󠆺󠆤ⷷ󠅼󠅕󠇥󠆢󠆱󠄊󠆪󠄺󠆯󠅧󠆭󠅕󠅐󠇖󠇕󠆵ⷵ󠄺󠆫󠅳󠅡󠆿󠅦󠅥󠇩󠇐󠄯󠆛󠇢󠅽󠇖󠆩󠄦󠅣󠄬󠄝󠅴󠅝󠅓󠅜󠆭󠆠󠄝󠅷󠆚󠄭󠆀󠆢󠇭󠄚󠅺󠅻󠆟󠆕󠄫󠅸󠆅󠄡󠇒󠄫󠄌󠄜󠇞󠅨󠆄󠆪󠇇󠇬󠆪󠄔󠆻󠄆󠇡󠄲󠅁󠇣󠄮󠆮󠆫󠆬󠅛󠄵󠅐󠆦󠆤󠅶󠄎ⷽ󠅝󠄲󠅽󠄽ⷳ󠆋󠅳󠄱󠅗󠆳󠆓󠇎󠇫󠅦󠆑󠅵󠅑󠅽ⷵ󠇓󠄤󠅸󠄺󠅡󠄑󠄦󠅟󠅥󠅥󠄫󠄦󠆲󠅫ⷵ󠇆󠇂󠅓󠅯󠄨󠄹ⷵ󠆌󠅢󠇓󠇏󠄤󠄳ⷵ󠆶󠅜󠅝󠆕󠇅󠅌󠆽󠅁󠄕󠄿󠇆ⷻ󠅒󠇜󠄸󠅷󠆉󠄳󠆓󠄑󠅳󠅀󠆟󠆚󠄃ⷾ󠄊󠇪󠄆󠄡󠄴󠄧ⷼ󠄥󠅙󠇁󠄏󠇝󠆀󠄘󠇂󠄏󠅓󠇂󠅬ⷱ󠆗󠄮󠆕󠆢󠄄󠆤󠅎󠆲󠄚󠄓󠅣ⷵ󠆪󠅛󠆮󠆺󠆤󠄬󠇚󠄮󠅊󠇗󠆅󠄨ⷳ󠅔󠇉󠆫󠄬󠄪󠇑󠆲󠆸󠆘ⷽ󠆘󠅉󠆊󠄹󠅪ⷳ󠆴󠇭󠅲󠄠󠆞󠄖󠅭󠇖󠅵󠇫󠅈󠆎󠆓󠄦󠅚󠄴󠆋󠄂󠅦󠄠󠆽󠄫ⷲ󠇮󠄦󠆩󠇛󠇩󠆵󠇨󠅒󠅝󠇚󠄖﻿󠄒󠅑󠄼󠆝󠇕󠇥󠅪󠅑󠆵󠆚󠆊󠄙󠆙󠅂󠇧󠆢󠇩󠆢󠇧󠄰󠄿󠇝󠆺󠄔󠇓󠅗󠄇󠄧󠇁󠆳󠄠ⷼⷵ󠇟󠄿󠆇󠇁󠅓󠄏󠄚󠄪󠅎󠄎󠅏󠄏󠇏󠅢󠄟󠄤󠅛󠄮󠅅󠆕󠅇󠆏󠅅󠅨󠄄󠅨󠅖󠄕󠆄󠄗󠅕󠄸ⷽ󠆩󠄮󠆪󠆈󠇡󠅢󠇒󠆢󠅻󠆅󠆳󠆯󠆄󠇃󠇯󠅓󠆹󠆤󠄴󠅯󠅄󠄟󠆐󠄍󠅈󠆯󠅅󠄥󠄚󠆘󠆎󠆔󠄛󠄁󠇪󠆼󠆎󠆘󠄉󠅐󠇛󠆔󠅖󠅎󠄢󠄕󠆖󠇟󠆸󠄫󠆚﻿󠆳󠅦󠄥󠄔󠇃󠅋󠇕󠄘󠄟󠆱󠆍󠆞󠄢󠅓󠄗󠄤󠄉󠆢󠅒󠄭󠇪󠆃󠅛󠆓󠅂󠅕󠆱󠅌󠅡󠄺󠇪󠄦󠇒󠆝󠇇󠄽󠆾󠇃󠄍󠆋ⷳ󠇬󠇤󠇠󠇭󠇙󠆖󠇗ⷶ󠆆󠆄󠆷󠄍󠄶󠆚󠅮󠄛󠄒󠆝󠄀󠇍󠆿󠄇󠄁󠅈󠇆󠇩󠅇󠆩󠆐󠅷󠆛󠄌󠅫ⷾ󠅾󠅸ⷰ󠅦󠆻󠄱󠆣󠇚󠇊ⷺ󠅐󠇋󠄓󠅍󠆏󠄖󠄧󠆾󠅄ⷴ󠆁󠄂󠅡󠅹󠄍ⷶ󠅅󠄆󠇋󠅡󠄑󠅋󠄤󠇬󠄲󠅫󠅄󠇕󠆵󠅉󠄸󠄉󠆤󠆲󠆤󠆨󠇥󠅜󠅌󠄍󠅛󠆫󠄓󠄽󠄫󠆒󠇬󠄞󠇙󠆨󠅖󠆺󠅳󠅙󠄠ⷻ󠅆󠄝󠆓󠇖󠄳󠆂󠅎󠅡ⷽ󠄵󠆬󠄞󠅡󠆚󠆖󠆢󠅊󠅓󠅠󠇪󠅝󠅝󠆉󠇘󠅞󠆔󠇍󠇚󠆼󠆌󠅶󠄌󠇔󠆦󠅓󠅗﻿󠆠󠆊󠇇󠅢󠅍󠆑ⷸ󠄰󠄓󠇋󠆎󠅬ⷺ󠅡󠇓󠇔󠆍󠇛󠇃󠄒󠇝󠆅󠇏󠄯󠅂󠆘󠅦󠇨󠄰󠄒󠅿󠄈󠅘󠅈󠅣󠄈󠅿ⷽⷹ󠆗󠇐󠄬󠅮󠅭ⷻ󠄓󠄒󠆵󠆂󠅌󠅵󠅹󠆄󠆔󠆓󠅀󠆯󠆂󠅱󠇝󠇓󠅞󠇄󠅌󠆯󠄪󠆒󠇃󠄃󠅻󠇋󠇝󠇀󠇃󠇠󠇚󠆃󠅁󠅁󠅕󠆐󠅕󠅹󠄐󠆡󠅑󠆕󠆫󠆞󠄭󠅵󠅌󠇥󠄣󠆃󠅦󠅊󠄰󠆀󠆫󠆪󠆋󠇐󠇘󠇄󠆸󠄎󠆟󠇯󠆜󠆞󠄷󠇇󠆯󠅏󠆷󠅻󠅻󠅻󠄛󠆠󠆤󠅯󠅛󠇅ⷻ󠄫󠇎󠅂󠅀󠅻󠅳󠇞󠇃󠄁󠇩󠄂󠇒󠄄󠄺󠆰󠇀󠄮󠅽󠄋󠆆󠅮󠆅󠄆󠄨󠆭󠄞󠄘󠅻󠅲﻿󠇚󠆔󠄸󠄣󠆴󠆆󠇘󠇖󠆫󠅦󠄦󠇧󠆉󠆟󠅓󠄄󠆋󠆜󠆩󠅁󠄿󠅂󠅵󠄏󠅐󠅌󠅮󠇈󠅑󠆋󠅤ⷷ󠆢󠇚󠅰󠆩󠅙󠄕󠇖󠄼󠅰󠆀󠆤󠆁󠄳󠄕󠆨󠆴󠅉󠄋󠄕󠄢󠆏󠇒󠄂󠅜󠅁󠅪󠇊󠄝󠅛󠄾󠄉󠅮󠇅󠄺󠄩󠆳󠇅󠅕󠆞󠄑󠇭󠄾󠅽󠅎󠅑󠇁󠅺󠆺󠅅󠄖󠄝󠇖󠅧󠄮ⷱ󠇚󠆴󠄅󠅙󠅁󠄐󠇒󠅆󠄆󠅞󠅃󠆳󠄳󠇙󠇕󠄹󠅳󠄍󠆋󠄏󠆙󠆀󠇨󠄥󠇈󠆋󠇆󠅓󠄡󠄙󠄬󠅀󠄽󠆸󠇡󠆬󠇩󠇚󠆻󠆢󠆻󠆉󠅠󠇭󠆄󠆬󠅹󠅘󠄁󠄌󠅙󠇅󠆎ⷶ󠅱󠆌󠇡󠆫󠄮󠄗󠇇󠇮󠅬󠅀󠅝󠅗󠅔󠄫󠆡󠄋󠅕󠄠󠇑󠇫󠅛󠅶󠅍󠆈󠄒󠅪󠇜ⷺ󠆰󠇓󠅲󠅖󠄾󠄀󠇆󠆾󠅥󠅹󠆕󠆵󠇢󠆐󠄞󠅁󠆜󠅁󠇖󠄆󠅢󠄈󠇆󠄰󠆧󠆍󠅂󠆢󠄵󠆓󠇝󠇙󠄣󠆌󠄈ⷰ󠄱󠅡󠇠󠄘󠆅󠆥󠆛󠇐󠄒󠄣󠆻󠅪󠆦󠇁󠄶󠄒󠅄󠄢󠇍󠆄󠆔󠄨󠄾󠇟󠄋󠇂󠅚󠇤󠄇󠇔󠅤󠇋󠄒󠇃󠅋󠄢󠇡󠇉󠆕󠆑󠅣󠅡󠄖󠄧󠅺󠄍󠄦󠆺󠄓󠄯󠆘󠄴󠇁󠆟ⷼ󠆞󠅘󠅒󠇐󠅏󠅤󠄐󠄒ⷸ󠆓󠄚󠅺󠆯󠆉󠇥󠆙󠅰󠅦󠄶󠆵󠆤󠄫󠆝󠆇󠆡󠅔󠄶󠇄󠆔󠄘﻿󠄫󠆧󠄻ⷺ󠄞󠇇󠅄󠆮󠅤󠅢󠆼󠅊󠄼󠇘󠆁󠄶󠄐󠆧󠅯󠆿󠅾󠅷󠅰ⷶ󠇝󠇉󠇡󠄶󠄂󠅿󠄑󠄻󠆖󠆱󠇐󠇑󠆿󠅣󠆺ⷶ󠄭󠅭󠄖ⷳ󠇢󠅃󠄒󠅲󠅖󠆣󠆂󠄗󠆗󠆬󠅮󠄠󠄎󠆄󠅰󠅯󠆾󠆪󠅨󠅙󠆏󠅀󠅤󠇭󠆺󠆚󠄅󠄨󠆻󠅁󠄘󠆇󠄚󠅭󠆧󠆩󠅚󠆈󠇮󠆦󠇎󠄇󠄪󠆮󠅖󠅅󠇙󠄕󠆆󠇤󠄦󠅫󠆇󠄼󠇥󠄀󠄳󠄶󠄛󠆶󠅣󠅐ⷵ󠆡󠄝ⷰ󠅪󠅑ⷾ󠇣ⷰ󠇇󠄟󠆎󠅏󠄠󠆘󠇢󠅦󠅛󠅙ⷼⷺ󠇠󠇨󠇨󠇠󠇕󠇑󠇡󠅶󠆃󠄝󠅮󠄷󠆩󠇭󠄬󠅉󠅙󠅺󠆓󠇝󠅪󠄻󠆶󠅄󠄓󠆑󠆜󠅟󠇊󠄎󠇉󠅊󠄮󠇫󠄶󠆭󠆫󠅲󠄍󠆆󠄒󠆪󠆳󠆮󠆖󠅙󠆔󠇝󠇦ⷶ󠇎󠅯󠆂󠆾󠅗󠆛󠅆󠄬󠅜󠆠󠅱󠆄󠆞󠆦ⷴ󠄢󠇀󠆤󠆶󠅓󠅚󠄕󠅭󠇤󠆺󠅛󠆪󠆟󠇞󠄖󠅠󠆞󠇀󠇓󠄪ⷹ󠅾󠆫󠆨󠆦󠇟󠄞󠆟󠆾󠄽󠅻󠅻ⷼ󠇮󠇠󠄨󠄽󠅾󠅷ⷴ󠆣󠅫󠅣󠇆󠅹󠇖󠄌󠇩󠇩󠄞󠅭󠇫󠅇󠅆󠄠󠄓󠆕󠆥󠄌󠄨ⷲ󠆧󠅊󠆉󠇣󠄇󠅲󠅢󠆤ⷷ󠇀󠄑󠅿󠅿󠅰󠆒󠆚󠅑󠄏󠄎󠆸󠄿󠄁󠅮󠄯󠄴󠇠ⷻⷺ󠆑󠄚󠅅󠅢󠄥ⷷ󠄰󠄆ⷾ󠄸󠄁󠄽󠇝󠄩󠆠ⷻ󠄸󠅷󠇐󠅻󠆺󠆛󠅪󠅭󠆊󠇨󠄩󠆶󠅒󠆪󠅻󠅧ⷷ󠆑󠄳󠆛󠄵󠇗󠄭󠄦󠅠󠅃󠇖󠅬󠄒󠆨󠆶󠆜󠅟󠄐󠅴󠅬󠄭󠄑󠆑󠄏󠄚󠅁󠅉󠆵󠅑󠇘󠇛󠅞󠆓󠆞󠆍󠇄󠄵󠇄󠆶󠄠󠇍󠄪ⷰ󠇟󠄙󠆹󠇛󠆢󠆥󠆀󠅊󠅍󠇪󠆩󠄒󠇐󠅔󠄬󠆖󠆝󠅥ⷵ󠄕󠄷󠇁󠆳󠄤󠄘󠅠󠄨ⷸ󠇤󠆥󠄚󠆉󠅎󠄩󠅌󠄯󠇑󠅠󠇟󠄪󠇉󠆐󠄆󠅊ⷵ󠄰󠅬󠅬󠅺󠄓󠄶󠅠󠅸󠄾󠅢󠅉󠄼󠅒󠄗󠄟󠆴󠄬󠆰󠄯󠆹󠄴󠄞󠇑󠆑󠇗󠇓󠅰󠅻󠆀󠅾󠇋󠇆󠆚󠆙󠅠󠆓󠇭󠄐󠅪󠄆󠇇󠄧󠇛󠆰󠇪󠅍ⷶ󠅽󠅌󠇮󠇯󠆚󠅫󠆿󠇗󠆸󠇇󠄑󠅌󠅰󠆶󠄪󠆻󠄇󠆳󠄣ⷾ󠆹󠆂󠆥󠄝󠄤󠅁󠆘󠆄󠅣󠇣󠄚󠄁󠇡󠅐󠄬󠅄󠇚󠄇󠆏󠅮󠇃ⷽ󠅭ⷽ󠄱󠅲󠆊󠇬󠄌󠅁󠆏󠅍󠇭󠄪󠆹󠇋󠇘󠇖󠅤󠅋󠅂󠆖󠅬ⷴ󠅾󠆒󠆊󠆒󠅍󠄝󠄹﻿󠅅󠆝󠆯󠅊󠅡󠆒󠅽󠇔󠆴󠆐󠅷󠆗󠅃󠄫󠅓󠄐󠆴󠄕󠅔󠅆󠇐󠇑󠇬󠇆󠄋󠇮󠄁󠆜󠆊󠆧󠇗󠄐󠇢󠄬󠆣󠇘󠄉󠇨󠄙󠅪󠄚󠅺󠄴󠇖󠆐󠄜󠇚󠅳󠇜󠄠󠆰󠆈󠄮󠆟󠇜󠅇󠇡󠇮󠄂󠆀󠅝󠅩󠅗󠅗󠅑󠅸󠅾󠅱󠅱󠅷󠅱󠄱󠆽󠅼󠄆󠇣󠅂󠇆󠇩󠇓󠄞󠅼󠅬󠆭󠆳󠄑󠇑󠇨󠄝󠄄󠄒󠆌󠅭󠆩󠆈󠄋󠅧󠄧󠇈󠄂󠄞󠆈󠆗󠄤󠅫󠄮󠄃󠆃󠆱󠇓󠇫󠇣󠄷󠄺󠅀󠅒󠇦󠅕󠄇󠇒󠅾󠄎󠄼󠄐󠄻󠅋󠄼󠆥󠆬󠅀󠇅󠅄󠄦󠅧󠅖󠅁ⷲⷱ󠆩󠄟󠄡󠅏󠄠󠅽󠇈󠅅󠇅󠇬󠅱󠇌󠇬󠄥󠅋󠆚󠇛󠅹󠅖󠆔󠅠󠆪󠆻󠄚󠅥󠄗󠇘󠅩󠅵󠆰󠄡󠅹󠆈󠄘󠇗󠆰󠆰󠆹󠅷󠆶󠅀󠄤󠇯󠆘󠄬󠅘󠆼󠇊󠄦󠇎󠇖󠄈󠄬󠄽󠆔󠅿󠆏󠄉󠆝ⷽ󠇈󠆄󠅣󠅊󠄻󠆐󠆑󠄣󠅖󠆢󠆟󠅓󠆇󠆼󠅎󠅓󠅊󠇨󠅅󠅅󠇛󠆕󠇕󠅵󠅤󠄒󠄕󠄫ⷳ󠆆󠅵󠇘󠄔󠆔ⷵ󠇡󠆛󠆗󠅐󠇓󠄚󠄥󠅧󠇫󠆮󠅚󠅊󠇬󠇇󠆒󠆷󠆁󠆝󠄅󠄺󠅈󠇑󠅣󠆲󠅐󠄽󠄎󠅵󠄍󠆃󠆠󠅰󠆝󠇞󠅙ⷻ󠆰󠅳󠅼ⷲ󠆔󠄪󠄈󠅺󠇦󠅜󠅯󠅀󠅬󠅭󠆍󠆓󠇓󠅆󠆎󠄞󠅌󠇙󠅆ⷷ󠆪󠄦󠇐󠇣󠆪󠄓󠄟󠄺󠆵󠇃󠅐󠄴󠄭󠅯󠅤󠅏󠆂󠄔󠆗󠅙󠇛󠄥󠅘󠆍󠇡󠅴󠅗󠆐󠄹󠆢󠇝󠄩󠄓ⷾ󠆴󠄝󠅦󠄡󠆸󠇐󠆝󠅝󠅣󠄃󠄔󠇇󠇁󠇋󠇠󠇅ⷳ󠇧󠅽󠇅󠇓󠅍󠇎ⷷ󠆡ⷾ󠅒󠅭󠆼󠇓󠇎ⷼ󠇏󠆿󠆸󠇩󠆈󠅮󠇛󠆟󠅠󠆙󠄪󠄍󠅌󠆯󠆜󠄤󠆒󠆒󠇙󠇟󠇫󠄯󠄀󠆐󠆬󠆑󠄤󠅥󠆌󠄺󠄌󠆢ⷲ󠄝󠆛󠅺󠅎󠅎󠆡󠄚󠇟󠆳󠆏󠇗󠇫󠇗󠇤󠅎󠆁󠆽󠄧ⷷ󠄇󠅙󠆍ⷻ󠅻󠄏󠇘󠇜󠇛󠄁󠆻󠆏󠄛󠅣󠇎󠅦󠄟󠄔󠅨󠇬󠆋󠇊󠇟󠄽󠅴󠇁󠅷󠄀󠆻󠆹󠄞󠄯󠄞󠅻󠇝󠅠󠄺󠄴󠄁󠄃󠆆󠆖󠄨󠅹󠅮󠆦󠆥󠅨󠇁󠅐󠅴󠅙󠄵󠇓󠇍󠅱󠅑ⷴ󠆻󠇜󠅓󠇮ⷶ󠇬󠅤󠄛󠅮󠇤󠅱󠆀󠅤󠅵󠅏󠆁ⷱ󠆹󠇅󠆘󠅩󠇑󠇖ⷸ󠇝ⷱ󠆻󠇃󠄭󠄶ⷱ󠅃󠅝󠅍󠆏󠇜󠆎󠇓󠆟󠆝󠅼󠅷󠆸󠇅󠄦󠆣ⷴ󠆔󠅒󠆌󠄃󠅼󠅵󠅰󠅴󠅺󠆸󠆥󠅆󠆽󠄝󠆉󠆞󠄼󠆢󠆢󠇪󠄦󠇁󠆼󠆬󠆳󠄮󠄞󠄐󠆌󠄞󠇔󠅷󠇟󠆼󠄺󠄼󠇙󠅮󠄆󠅎󠄹󠄆󠅡ⷳ󠅢󠇖󠆍󠅻󠄿󠆬󠇭󠇏󠆢󠆚󠅀󠅘󠆘󠄯󠇢󠅱󠅨󠄼󠄯󠄜󠆇󠇆󠇚󠆇󠅀󠇋󠅣󠆟󠄄󠅏󠆧󠆬󠅽󠆺󠆬󠆺󠆆󠇀󠇦󠆪󠇉󠅦󠆷󠇠󠅽󠄨󠅦󠇀ⷰ󠅠󠆾󠄪󠅋󠅺󠆉󠇂󠄯󠆣󠇩󠇓ⷸ󠅥󠄸󠅑󠄈󠆚󠇓󠄁󠇒󠅱󠅹󠆒󠄁ⷽ󠆲󠅯󠅨ⷻ󠄘󠄲󠅤󠅹󠄑󠄻󠆶ⷷ󠆥󠄳󠄅󠄾󠄺󠆪󠆱󠄺󠇘ⷲ󠅂󠆂ⷾ󠄌󠇀󠆣󠄫󠄤󠅫ⷹ󠆰󠇐󠅞󠄆󠆟󠄏󠆘󠅕󠅗󠇝󠄎󠅏󠅎󠆎󠅏ⷶ󠇁󠆹󠇗󠄐ⷷ󠅁󠇬󠆴󠄎󠄪󠆰󠇙󠄢ⷷ󠅕󠄅󠅍󠄛󠅚󠅱󠇨󠅵󠆇󠆺󠅱󠅄󠆳󠇙󠅺󠆚󠇖󠆉󠅅󠆛󠅠󠅰󠇬󠅚󠆂󠅛󠆏󠅿ⷴ󠅌󠆞󠆭ⷰ󠅛󠆄󠆼󠇉󠄽󠄉󠇞ⷳ󠄮ⷷ󠅬󠅊󠇠󠅑󠇬󠆸󠅝󠇗󠇟󠅒󠄋ⷲ󠆣󠇦󠇤󠆍󠇊󠇢ⷻ󠇆󠆡󠅢󠅶󠆍󠇠󠇌󠆥󠄷󠅊󠄺󠇞󠅍󠇌󠅉󠅰󠄔󠅢󠄩󠄞󠄠󠅫󠄝󠄆ⷼ󠆢󠇛󠅎󠅸󠄐󠄅󠇦󠄪󠇌󠆜󠆊󠅏󠄫󠄼󠄬󠄦󠅛󠆨󠅩󠄣󠅉ⷼ󠆉󠅚󠄀󠆻󠅙󠄅󠆻󠅍󠅼󠇠󠆃󠆁󠄛󠅣󠇛󠇖󠄬󠅫󠄁󠆖󠅭ⷷ󠅟󠇐󠆬󠅲󠇈󠄼󠆸󠇃󠄼󠆿󠄜󠇒󠆫󠆞󠅻ⷱ󠆘󠄧󠅩󠅃󠄱󠆊󠄛󠄻ⷹⷽ󠄵󠇥󠅼󠆷󠆢󠅜ⷾ󠇏󠇨󠇉ⷹ󠇃󠇕󠇤󠅲󠅐󠅋ⷴ󠅉󠅸󠄪󠇧󠆊󠅓󠅊󠄺󠅞󠅈󠆧󠄦󠇃󠅔󠄲󠇦󠅷󠇥󠅼󠄱󠄔󠆔󠄥󠅼󠇁󠄀󠄨󠅨󠄛󠄽󠆵󠅩󠇯󠄳󠄯󠆪󠄯󠅎󠇙󠆶󠄻󠄭󠄪󠅓󠄰ⷲ󠅶󠄺󠅊󠆪ⷳ󠆖󠇞󠅡󠅼󠅪󠅴󠅟󠅭󠆥󠅓󠄱󠇧󠇓󠅍󠇭󠇮󠆥󠇓󠅼󠆁󠄬󠄿󠅌󠆂󠆫󠆬󠄕󠆄󠆃󠆳󠄧󠆪󠇕󠆂󠅮󠅯󠅄󠅚󠅐󠅈󠇚󠇏󠆭󠆉󠆘󠅢󠅂󠆔󠆕󠆅󠇑󠇢󠄁󠄊󠅤󠅎ⷽ󠇌󠆺󠅷󠇜󠆆﻿ⷸ󠆄󠇈󠆙󠄵󠄍󠆦󠅏󠅫󠆆󠄮󠆔󠇈󠄸󠄟󠆷󠄽󠄒󠅕󠄃󠅾󠅼󠅶󠆛󠅒󠅙ⷴ󠅧󠆽󠅼󠇨󠇝󠄚󠄺󠆾󠄢󠆆󠆝󠇣󠇩󠇂󠆈󠆞󠆜󠄣󠅅󠅝󠄷󠆝󠅃󠅾󠅙󠄹󠅠󠅦󠄈󠇞󠆡󠆮󠆼󠆢󠆄󠄔ⷻ󠆁󠄳󠇇󠅽󠆸󠇭󠆾󠅕󠆈󠇪󠅞󠇕ⷽ󠄸󠇙󠅡󠄄󠆓󠇚󠄔󠇥󠄉󠄩󠆍󠅿󠆦󠆙󠄋󠅫󠇍󠄎󠆓󠇄󠅎󠅚ⷺ󠆐󠅱󠆈󠄏󠅋󠅈󠆑󠅚󠇈󠆛󠇌󠆵󠄂󠅄󠅔󠄪󠄹󠅾󠅄󠇜󠅺󠆹󠄌󠅟󠇐󠇢󠆖󠇉󠅹󠅆󠆚󠆘󠆡󠇪󠅑󠆉󠅎󠅵󠆦ⷲ󠄼󠇏󠇤󠄫󠆙󠄺󠇄󠇥󠇝󠄗󠅙󠆿󠄋󠅈󠆃󠇈󠄫󠅴󠄫󠇃󠇣󠄘󠄁󠆷󠄱ⷻ󠆪󠄖󠆳󠇃󠆷󠆝󠆆󠄆󠄞󠆅󠇟󠄒󠆝󠅵󠄲󠄟󠅎󠄜󠄬󠅳󠅢󠄮󠄻󠆒󠇉󠆘󠄽󠅨󠅧󠆀󠆏󠇪󠅜󠆁󠄸󠆽󠇛󠅨󠅣󠇝󠅛󠆇󠇧󠆶󠆰󠄞󠇓ⷹ󠄛󠄉󠅡ⷷ󠅭󠅣󠅹󠅷󠄅󠄆󠅁󠄠󠅁󠇇󠆃󠇞󠄡󠇭󠅑󠄻󠄡󠄻󠅕󠅇󠄝󠇭󠅞󠄚󠄒󠇎󠆭󠅇󠆧󠇝󠆥󠇠󠅑󠇊󠅳󠅄󠅯󠅕ⷰ󠆅󠄬󠇢󠅰󠆻󠇯󠄬󠅒󠇂󠄅󠅈󠄅󠅍󠅬ⷺ󠆢󠅻󠇀󠆎󠆎󠆝󠆱󠄓󠄆󠇍󠆇󠄽󠄊󠄟󠄴󠄜󠅡󠅠󠆤ⷹ󠆽󠆛󠄎󠄼󠄵󠄃󠄶󠄵󠄗󠇋󠇮󠇆󠆱󠆼󠇊󠆄󠇎󠅖󠄍ⷺ󠄣󠅮󠄖󠅫󠅶󠅒󠇤󠆥󠆁󠆤󠇃󠆥󠆵󠇭󠆙󠇚󠄎󠅷󠅳󠅞󠇓󠄃󠅽󠅎󠇧󠇩󠄕󠆰󠇡󠅸󠅎󠄬󠅷󠆔󠅈󠆉󠆳󠆍ⷴ󠇓󠄤󠆐󠆺󠅤󠇭󠇮󠄽󠅪󠅂󠄫󠇢󠆰󠄊󠇤󠇅󠄚󠄍󠄼󠆽󠄕󠅫󠄌󠇦󠄇󠄷󠇋󠆼󠄰󠅏󠆒󠆜󠄣󠇖󠆥󠅤󠅅󠆓󠄍󠅯󠆝󠇉󠅋󠄐󠄎󠅥󠇜󠆿ⷸ󠄵󠆰󠆓ⷶ󠄛󠄶󠇑󠆬󠇝󠄮󠅫󠄇󠅍󠄟󠅏ⷱ󠇖ⷵ󠇅󠇅󠆇󠄗󠅗󠄗󠄗󠇧󠄗󠄗ⷹ󠆳󠇨󠄋ⷼ󠆌﻿󠆺󠇀󠇠󠄓ⷾ󠆈󠅊󠅞󠆞ⷾ󠄡󠆓󠄎󠅩󠅯󠅯󠅏󠇞ⷻ󠇠󠅣󠅿󠅊󠆱󠅱󠅯󠅖󠅼󠇈󠄖󠇠󠇣󠆂󠅕󠅵󠅛󠇕󠅷󠆕󠄌󠄗󠅚󠅨󠇏󠅖󠄚󠅹󠄂󠄟󠅟󠅴󠅩󠄚󠆵󠆢󠆜󠅏󠆂󠆧󠅏󠇕󠇍󠇔󠇛󠄻󠄼ⷹ󠆳󠄯󠅣󠅁󠆃󠅩󠇪󠅖󠄧󠇮󠆫󠇗󠅖󠇞󠅖󠇞󠅬󠅇󠄰󠆊󠄪󠅝󠄶ⷵ󠄵󠅺󠄻󠇫󠅨󠆕󠆹󠆢󠅻󠆘󠇌󠆕󠆫󠇉󠆨󠇀󠅷󠅙󠄷󠆈󠇢󠄪󠄵󠅷󠄆󠇖󠄘󠆂󠆷󠄛󠅑󠇚󠄾󠅘󠄟󠆦󠅘󠄽󠅢󠆎󠇝󠇫󠅐󠄵ⷼⷲ󠆇󠆃󠆳󠇀󠄈󠆙󠄅ⷹ󠇒󠄢󠆷󠆺ⷱ󠄠󠅰󠇊󠆒󠅹󠅸󠇖󠆬󠆝󠇠󠄄󠇆󠄐󠅼󠄪󠆁󠆔󠆟󠄇󠅤󠆯󠇉󠄔󠇂󠇔󠅢󠅞󠄈󠄰󠅍󠅾󠅣󠆘󠅟󠄩󠄂󠆰󠅚󠄎󠆝󠇓󠅮󠇪󠇜󠅯ⷽ󠅆󠇁󠄩󠄔󠆈󠅭ⷷ󠄯󠄪󠆭󠇝󠆸󠇛󠇀󠆗󠇞ⷺ󠄼󠅱󠆝󠇕ⷽ󠅍󠆑󠇛󠆮󠄯󠄰󠇋󠆈󠇬󠆨󠆴󠆉󠆱󠄏󠇏󠄾󠇊󠇂󠄡󠇙󠇩󠇫󠅤󠄚󠇏󠆧󠇃󠇕󠇜󠆣󠆪󠇪󠇪󠆓󠇬󠇪󠆪󠄑󠇯󠄋ⷰ󠆹󠄹󠇛󠄆󠇮󠄿󠆯󠅧󠄐󠅡󠇋󠇣󠄌󠄟󠄌󠄣󠆪󠄞󠆘󠅵󠆎󠄑󠇔󠇠󠄖󠄂󠅵󠇛󠅦󠄢󠄇󠅃󠆗󠄕󠅱ⷱⷹ󠅰󠆼󠆵󠇫󠇋󠇆󠇡󠆀󠆌󠆜󠄂󠅤󠄎󠇥󠄏󠅂󠅺󠆼󠆑󠄻󠆰󠇀󠅠󠅂󠇮󠄂ⷼ󠅃󠆢󠆻󠄛󠇑󠇀󠇪󠆾󠄑󠅪ⷺ󠄑ⷻ󠄮󠅫ⷹ󠇆󠅾󠇮󠆃󠅱󠄬󠇤󠆃󠇡󠇅󠄃󠄙󠄦󠇭󠆐󠄸󠄀󠄺󠇚󠄶󠄫󠅗󠄸󠇣󠄥󠆦󠇍󠅬󠅃󠄇󠄤󠄋󠅋󠇆󠄢󠆒󠄋󠇈󠅢󠄗󠄦󠅩󠅔󠅙󠅻󠆚󠇘󠄵󠇃󠅘󠅼󠆥󠄾󠇠󠇓󠄈󠆲󠅹󠄢󠇋󠅱󠇎󠅨󠄢󠆡󠇌󠅇󠆺󠅮󠆲󠆵󠄅󠆕󠄗󠄭󠇝󠆣󠄣󠅛󠄼󠅟󠆕󠄊󠆰󠅠󠅸󠆰󠅜󠅭󠅝󠆊󠆾󠇒󠅀󠅫󠄋󠅅󠆠󠄔󠅦󠄽󠆔󠆶󠄇ⷳ󠄚󠅥󠇦󠄯󠇭󠆲󠆆󠄙󠅫󠇇󠇗󠅾󠄔󠄏󠄬󠅵󠄢󠄊󠆌󠅳󠄜󠇁󠆾󠄮󠇫󠄫󠄋󠇜󠄂󠇠󠄚󠄋󠄡ⷴ󠆭󠆫󠄲󠇞󠄰󠆦󠄔󠆒󠄦󠅨󠆔󠅇󠅞󠅖󠅊󠄶󠆭󠇯󠇎󠅴󠄛󠆚󠄅󠆫󠆌󠄭󠄬󠄪󠆨ⷱ󠄴󠇨󠄰󠇐󠇡ⷴ󠄜󠄍󠄆󠅤󠅐󠄲󠅸󠅒󠅁󠆼󠇍󠇪󠇥󠄺󠇒󠆄󠅓󠄹󠆲󠆈󠄐󠆭󠆻󠆟󠅸󠆲󠇋󠅭󠄞󠄊󠆵󠇣󠆤󠅤󠄼ⷻⷽ󠇌󠅍󠇭󠅨󠆂󠄸󠅮󠅖ⷱ󠄔󠅏󠆴󠄉󠇃󠇨󠄤󠇒ⷲ󠆊󠄾󠅓󠇒󠆙󠆘󠄠󠇋󠅠󠅂󠄔󠅰󠇤󠅪󠅀󠅨󠄤󠆬󠄄󠇁󠄂󠆮󠅁󠄃󠇭ⷳ󠆑󠄱󠆧󠇩󠇞󠄿󠇫󠅝󠆱󠆕󠆿󠇬ⷱ󠅿ⷽ󠆄󠇠󠄸󠅻󠅃󠅑󠅁󠄼󠄀󠆐ⷲ󠄀󠄓󠅮󠄏󠇋󠅯󠅙󠅦󠇫󠆔󠇫ⷴ󠄏󠅤󠅬󠄲󠆐󠆖󠅃󠄹󠅺󠅽󠇀󠅩󠇥󠅃󠇘󠆁󠄈󠅮󠄾󠅄󠄡󠆴󠆃󠄸󠇊ⷾ󠅑󠇕󠄐󠄦󠄎󠅯󠅨󠅾󠆜󠄫󠆷󠅳ⷼ󠄅󠅐󠇩󠇉󠅫󠅔󠇌󠅮󠆄󠅃󠆊󠆧󠅢󠆮󠇞󠄒󠆨󠇄󠆝󠆊󠆞󠆜󠄑󠄐󠆕󠆑󠆓󠄝󠄶󠄳󠆆󠅬󠇑󠇛󠅃󠅒󠆭󠄶󠅲ⷼ󠄡󠆬󠅝ⷼ󠅂󠆳󠆈󠇟󠆴󠆈󠇃󠅭󠅟󠄠󠆆󠄓󠄎󠆍󠄓󠇙󠇏󠆲󠅞󠅆󠇮󠄵󠅶󠅬󠇩󠅅󠆇󠅃󠇊󠇡󠆏󠆡󠅏󠄶󠅝󠄭󠅳󠇜󠄖ⷳ󠆕󠄉󠅛󠆂󠅴󠄓󠆈󠅻󠅡󠇉ⷶ󠇩󠅺󠄭󠅵󠄄󠅪󠄆󠇡󠄇󠅶󠆲󠆥󠄱󠅒󠆞󠅦󠇊󠆥󠇄ⷺ󠇙󠆋󠅃󠄟󠅠󠄩󠇥ⷲ󠅱󠅬󠆥󠆯󠇮󠆃󠅺󠇊󠄓󠄴󠆤󠆧󠆎󠇞󠅻󠄦󠇗󠆇󠇮󠇝󠆕󠆠󠅴󠇓󠅡󠆸󠄟󠅢ⷷ󠆙󠅡ⷵ󠇘󠇉󠆎󠅣󠅅󠄆󠅁󠆤󠆮󠇭󠇀ⷰ󠅮󠆆󠅖󠇯󠆙󠇕󠅤󠄓󠇎󠆱󠄦󠇜󠄏󠇤󠇯󠄢󠇃󠄎󠅺󠆃󠅗󠇬󠅴󠅋󠇨󠅵󠄻󠆅ⷶ󠅅󠅓󠅗󠇜󠄙󠇄󠇫󠇩󠇫󠇣󠆣󠇣󠄓󠅊󠆜󠅢󠅰󠆶󠅷󠆢󠆉󠅢󠅇󠇨󠆺󠆃ⷱ󠇄󠅘󠄲󠆦󠅛ⷺ󠆂󠄝ⷸ󠄅󠆣󠆟󠄓󠄘󠄳󠇎󠇊󠇤󠅧󠇌󠆖󠄨󠇨ⷼ󠅻󠅰󠇑󠇐󠆘󠆰󠅚󠄋󠇐󠄐󠇑󠇙󠄁﻿ⷲⷲ󠆡󠇩󠅹󠅏󠅁󠄆󠇍󠆲󠇙󠇛󠆤󠄾󠅢󠇛󠆗󠇣󠄄󠇤󠇅󠅻󠇭󠇎󠅽󠅯󠅣󠇣󠄪󠆿󠇄󠅭󠄬󠆐󠄬󠇏󠄿󠄎󠆠󠅬󠅯󠆊󠅹ⷷ󠅱󠄘󠇍󠇯󠆀󠅑󠄷󠄟󠇉󠇃󠇇󠄂󠆔󠄟󠄹󠄀󠅹󠄃󠅎󠆃󠆐󠅩󠅷ⷽ󠄑󠆚󠅞󠄓󠄳󠄹󠄋󠇉󠅸󠄗󠅊󠄝󠇉󠆿ⷸ󠇎󠅄󠇛󠅤󠅗󠆳󠇏󠄥󠇉󠇥󠇀󠄵󠅸󠄃󠄫󠄵󠄿󠇤󠄜󠆑󠄝󠅖󠄮ⷰ󠆛󠄓󠄯󠄪󠆡󠇐󠄌󠆟󠄸󠆯󠇁󠄧󠄨󠅺󠄨󠄟󠇬󠇝󠅶󠄱ⷱ󠄈󠇏󠇩󠄹󠆠󠇝󠇠󠅸󠇡󠆒󠅃󠇄ⷰ﻿󠄫󠇦󠇬󠄏󠅃󠆦󠄝󠆿󠅵󠄜󠅌󠇮󠄎󠅄󠅂󠅾󠇄󠅈󠄬󠅔󠄘󠇊󠇗󠅞ⷾ󠄳󠄺󠄖󠆘󠆿󠅰󠄴󠅱󠇘󠆑󠄩󠄴󠅙󠄁󠄌󠇪󠅟󠅠󠇑󠄽󠇊󠆱󠆰󠆃󠄷ⷲ󠅎󠄱󠅷󠅣󠆐󠅗󠄇󠄧󠅉󠆈ⷻ󠅿󠇧󠇏󠆿ⷸⷼ󠆏󠄋󠇎󠇍󠇨󠅸󠅈󠄖󠆿󠄰󠇅󠆸󠆡󠅣󠅊﻿󠄢󠅋󠄡󠅑󠄵󠄈󠆟󠇉󠅂󠆾ⷲ󠅣󠇊󠅟󠆨ⷲ󠇣󠅷󠆇󠆦ⷴ󠅏󠆺󠆿󠇯󠄎󠄍󠆰󠇂󠆠󠄓󠅼󠅓󠆬󠄠ⷰ󠅶󠆘󠄬ⷽ󠇌󠅰󠄡󠅯󠆥ⷷ󠇇󠆢󠅾󠄄󠇔󠇇󠇗󠇗󠆣ⷻ󠇬󠆫󠄽󠅗󠅃ⷴ󠆹󠆂󠆃󠆄󠇗󠆴󠅗󠆥󠆽󠆍󠅍󠇯󠄸󠅶󠅶󠆳󠆪󠅮󠅱󠅑󠇏󠆋󠄒󠇯ⷻ󠇣﻿󠄋󠄁󠆆󠅳󠄬󠆄󠄸󠆕󠄱󠄄󠄸󠇇󠄂󠇊󠄧󠅡󠇬󠆅󠄯ⷼ󠅫󠄶ⷾ󠄿󠄔󠄐󠅚󠆝ⷹ󠄩󠆊󠇄ⷻ󠆁󠅉󠄫󠇯󠄛󠄛󠅛󠄋󠄱󠇯󠄒󠇣󠄓ⷼ󠄩󠄭󠆍󠆆󠆏ⷼ󠄖󠅀󠅈󠄩󠆼󠄚󠄣󠄌󠆐󠄲ⷽ󠆄󠅴󠄆󠆬󠆰󠄊󠆈󠇣﻿󠄀󠄜󠄢󠄌󠅮'
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
