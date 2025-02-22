---
hide:
  - navigation
---

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
code = b'eJzVW/1u28gR/z9PQbh/kMzp1OSuH4DvmNZJfNegubhwnDsUtkHQ4srmmSIFkoqtCgLuIfoMfbB7ks7HfpOUnHOAogYskbs7v52ZnZ2Z/dC8qRdBnnXZrMzaVrRBsVjWTWeKnsiComqXYtap11pXNEI9tev2yRzxuvWyqK4V1FG1ngQny66oq6ycBGfrpXjyV4NPn8Ebhn9VV/Pi+vBJAH/tDVAfBld1XdJ7vqpy0VgFVZ3Xs9YqKOvq2nqd1bmwX7Oy1PRjDBx1XVNcrTrBPFTZAiDarqG3j1m5glcQiF5BTHgjeRR+dlWKXSwvm+Jj1tlN2uK6yrpVA2VKR+fQ3yXT1zO/OBdzNRbpvG4WWRfVVz9PgqcTVljyXVa2YiK7Vm+sKvWGelLPqCT9TBpSb/DCj/GhVCeOTeKMVMR90qfuk7+CukEI3Td/yc7xQzcgFvDDlDAj/CVLY2KiXnXLVZeURdtF6boQZZ4qbZRFJVpWBrMaM0kxR8uctl0OxNOizbpuHUmZaBhFsyhAv+ldkXc3Sd1Or0WX6tK2+JeI4umsLleLqtVUzMgUOhdNFz0D7XfrUkxfHp0GXwThr//+JQyeetBQcXr8/vgs9kGy5VJUefSpCI0Au6mC8KIKpz/XRRVFqIIArCKgh6KSHaAKuKSF0eiCd3UlQDloSnt1eKh0yO9TOYu0CEQf0LRPr0UlGjDvlBsB6ryOmFew3ZSmTyKtlt+4KzKJs2YllFxL1RgfsY0eSVMXJAmiUi2aiFuTQlWxTGHU6ibSncc9vsMNa/3s9OjN2ZYn+IZ0vA02mm4bEp2AybAHAUjG6UepkHebDGv+dnz0ersxUm1lfaj1if5HqxNfIvpAhbC+Bvsir+WwiCUSdpk1ouraJJwE0qZSnAxcTA1bqxM9KpJsj25UK925LJB9o41JFxpBpzBNGzaPME1LUaUpMMWWa83dZm1eRjsGatOpa39QxbJYQyTuZ2LZkWM/bpq6cXtYYszw+UUI0wyjRuKLgIUkQ/jrL/8JjQ/QASAhVSvIVJdHSDkJ9CwYtz0dSszwqiIpHrhg7gYeBuceCAVVQVblQYSuQs56dt4xlY8IzZTgJ1dVF6FPinEePts5PK9PXr3fHhwcbICSvm0T7884CwH9zXkPB7QLSBPowAK79D0YRhoSUHo9iAmUA2hX4khoidjWq2Ymx4mfUwSLnKHBcEN1DzBMbsiJimT3otpwqZkV1jhwTqSBM5WttEkLFSKP0gIiRmrKHV8+CW7FOimzxVWeEe0hfU7RwHq2RR4d5mcu8dq0BV1BJhIZdI3MsWRX38w0xibgAUNTXjSeBcn0AeohWGdN194V3U0EUydkw8MK4McqdoyPsw7fcrk4dgcD6rqiWgldKPOyft+ya0KUUOPOh2OWM/EBMPYdy8usFcf0CNoMsjYQQzCGOe0TEm2YHM0+wYcAHxMGjlFZugnNMHKrZhhsH0Ek0ktIjeLzXhA2Ij+pJleWGF4SCU+RjOIKszjRUzDRnXjp5USPmfyeWFrQT+QPEviXFrrXw/JIOCObWrgwrMppGGoTcOUARz+iFBQ7JiaMxIOQYQThINZzfcglHVpmKubFfRLykkUlJS5Z3UDSB2ncfFXxdB2GyNp1NQtQKYMwDjX6RFO1EN1NnQ9UXK2KEnrWNTdZOxQBB5ix2bAdvqoP7XxX+9C/H//zp5NTSJK42VYWvzp6+/bo5dvj7QY7VKXv33z/7ujswykUG+2bnEpbh+/XBwxC8qEEByomMnFA2cHJe98IJjAnckh6MlQum4XnAbSU86woRR50dQA9BHaoCDY0V0S8hUdhc++Edck7zgCLV9nECfewLsDZ22NCT2k5i6aUVUfO8oPo59Qh+4GUghQkbNi4uo7M7LOiCaRfTUGuDN+8KEFOAMm9xQIFqzGPNBAtaT9Ay2Shehzqmliv653eSdvUOT7FrjEGKmH/8ej0DdudDqraJE9eH2/lsCHyNkiCje5VDaDHVSfuOxU2i6blxdkkSCfQd9slWD2FDLoraJ5SxmVWSW2HMxCzW0MbBy+C58+e9U1Ntzg/hPpLtcqkZSjkqk8G2/aHVDqGgQGVw0J6MVlq3+RBl0Z3rmOk8h2pqZOIqsZ7stFev8YxBHZm+TtZjVnqA1LUHbCHmN45KSsUaOyLys+BXfAdwNKEnOlizxTM8CfgstD3JM/MsBQtuIYuq2a6OU6DfpcHyo2enW7DjVzUSlYPFBivvsecifbb707eHW+xiSOqTY/cjtOfnX443mKTUXrathoH+O7o7fvjLTXyIfr6gIDfwYqirLMuHlCMFurDDy+PT7ebgbX6IGxezLo+nBpArO2PohpAmJjP43Fo3Bwbh8bah0DLzQvKeax0M6uuIXW6arLZLcQbAJzdJI2YzldlSS9R+G00fRq/CCcKQXM6QDquT3KZ3/Zdax9jeg0ZzzJ6Hjve9oUzBD46mrHanvGSgP4IwKOrJGv6sNJeBF8PuFXX3I5PT09ODyGc15B1iWW5Dirw0iL3TQVdG/pt6HWHuZGMm83WtTTmHUBT4KopYFmIa2TXK9x6smBc8vyG3yLkdRsk7bxwm01hpbdoo/jSYdqJtiMMS3Y3ZoOpx7M7jp6EtEGZWFueIZbiTqm23zn5p+2EuYZHZLrfi8zUKtz8JK+okSIJ9aWaCrtlAQ9OXOGDgRsTwrYxayqWbfc/sLFyyFG4Yp5fjlgY8A3m1Ys4nhT2GEBvn2ow57vsBTlwjeXyM9sK9fBYQzl/uJ1cDpqJ3tpN5WAt6nxV8oI5naYpv6ap0i2/qziMeaAs4R1zoKD1Y2rT7pu4qi9ew213OlemYOTtdJRUL1p6u8upMX61hqRiWkUumtpdRM5pEZqL+0lwlbWCcHAYRbVa0HFEpBWFpN5WkJxg95Qeoq4sjBa3BGDZ5FLgX28DCf94z8MZNQ2m9x+GTkhkkt/g5oiqgZA+u02pLPqTDqH0bomOr4hhL/B0YURPziaZrpvOYXFZOWBGBG+XUh7DIcVh4IxxH257aBWiuVd1P2V2GMEVbYr6hPWMv0uXC2v6DpPEzpr0IXKI+yWsj1pYNJl9ckRUJvnQPU9mdrm6KosZLmfBG2ZkjBlanyHQq5+p3KkyS5hMbU/aRWp/SkZXSbSvh0F0D4o724/kb6X2eWKhecH3aLkNvCvxfngX2seR4j4ExpLYR8HjLTPG6CFc6f1Dr3D0rI9O9P5BxBYDh73pQVxCPTJqdT00Ux+wpWLPOlsQlHVMkkFpBtjaQbh3Z0Ar17Jv0q47+p+qXmUPD9Wv1fvnULAtDGl4TJr9Kt5P+WAdO2chPA0tX4Bad+dK75x8j9ZfS+AHKt3q+zPo3JYERXNF+QSN7yfcr3CKIAMhPBfL7sYJ9Cpiz1YNpj/cLFZJdpAiRw0sd11aKTO1tq9zuNxyD/Q5nadXwIaTqGG5E+uUkttIP02CruhK4ewkDw39hpptD/1VAh2CowzyYFIDT2/FGpaOljxj272a5ByxLiUrmmx4m1aeIjmUcf/gfGDX9jds2Fp3TKzdWqnmRkzb1VUUXlzcP7+6uDi/uMi/iL7Bz/gvC1zPwD9RyRtoP2Uy/zk4OJAHZ3y8Qps7eA4g7rMFXuNZVbdVfVfJ7LQN8KySb38F9RLzy7ppAYSDIDIKeWbRpWnUinI+CZ4+Vdd9bu+y5tqe7dhgmrrVifvqtZW3wjbbEYyiSpdNfY0ZF98ms7iiyy3MlWveaNV3WTeI4lo6dwa+EhYQN6K080B1PSq0esQtn16HquG3Px2dBUbzrN0XFrnVjQeB45jMw7Nm7STIIEPwewmkck1A9ppMYalUzAsB/stvDIMuVQCuzaFz2k2dS0M/KDiFAuurw4tKmzxufvFNgj5PXGd1f1PkdjQNzNwiZ6sChg/PvtTCId3pQ3qN59NhIt6jss6+ghrStUCdTk5k/3RpAyeRD4ceowdX1dWX2dVVIz4WEGBz9j8ydtQzWDTK4zkfjE8afN04JOT5FHcMKS/W9gSlGGGBwYDcBfiPRHc3ooEpfyPU8CP2XdbyzcjcB4NCx2Jm5QpHrcTtDHaOA+KA2VtEchJYXYJmRg2uZ01dM4wlLyDykRY5M5HlOIg0FFDmI1032dqCyouWbhiQk52vSn2jkeHB+7R1KfpWBK0tFIFamPVQ2h7MK9SZPz3LGrTejs/fKB6YrkQUmKg3gn1d1lcWuAXANRZC6HtI5YBBphQW39Aoj7zdDfJL/Til29AoWGXsJdHITLRAp49BoxcscOUEJYOHX8TbrF6uI004lZJFhGjdisGbB9zmoVA7Dt/Gd1G+crcIaIB4LawSJR5ok1/RcbYV2XymZEAw2ZPBhPD+1rWA0GhYKYIVXIMF2kduY4GPzvBMxPEvH8mb0f7dcATH0RuK7PEAQMoCJtwept+yzNYp10X85ZKBthzK/maZVJnTyoewkwncxIpCaAcJkn0BfQgTxRsaH+cy0hxvUJeevkbV7GYpZHgqb+pNgUrcqQzIkYCojJ7sfJgxZIveXqRqtZHyhzB38QvdIn7TJA63fYUYTjjnTWQ/y3oZuff7sKWX4Q0Zhy9Dn2y6Wua4veobE7YE7SaQ0MKU7dP1Wuos0gjhJ2eypXFSnmXKqcT22cslH+Ap5fRxfKVv7oN2ygM0ZKeO3Xsu14fuXbihdaTDcD9N7jPD5rGTHceLDIJIW9uBYaYI/onqI7OabMI51oSHgfwNSdhBb/CKnW4JvW6n0L5o6oo7g5w7fXXy9uSUVkQxBNs70USxo3TdwfiKVzKmW/qKHfgFiJ/XGzfOxuQvhS1V0JWKwUlDMmG1VqAhouMo/uXKQ9fd/k9Fkl0/9qAORn7r4atjn3fnRABHLy8+6lzAD1U2mgpq3MYCyfL8cQBle1PMu8dhNJ8Bo24eycNjAcpHCiBvJmsQigtuMEO/bRIuZxaa0ERrRwpOfiTSDt2dFueS5NLNYSjzM7By2oS8SORolwv85pUXlVBeh0/w8NDeOSDu6voTgq0Xs3aDJ0kQclYZ/n+lqX0x5Erlt8rB5K4gEvIRklioIMr33pJpVBYYv3B0rbFjcdFkBTCor7PT/d2xTIU39d7jco9BXh6dgvu+f351/uybr/+w4OUcnUzK4uemGPdxTOmfZSmsbQ3CV7KQL56Z8ueq/OTdsSn9o+7vw7EBVhh0e8QUKwi8oyhLvzJcyGvXfVnUxes+vr583Wdf7b8aoq8VHKyRTXtV2tvP9G4CzG5W1S3d4ijKDjIJ/KEtuMuxrOO9TDsgEBZQPgljL+PhnwbwT1QRWh03K4okdO28lb/+MB4W0uQlpjT4sySShk+bF0BIq34lIwhImwMJ2Qz4XpVDx/8Fh8zF7A=='
exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
```

Now you can use `wat` object.

!!! warning
    Before executing **Insta-Load** snippet, it's recommended to verify what you're about to run.
    You can either:

    - Verify what's inside the extracted code beforehand:
      ```python
      print(zlib.decompress(base64.b64decode(code)).decode())
      ```
    - Paste the content of [inspection.py](https://github.com/igrek51/wat/blob/master/wat/inspection/inspection.py) into your interpreter.
      It has the same effect.
    - [Install package with pip](#install-with-pip) and review the code.

### Install with pip
Alternatively, install **wat** package and import inspection tool from **wat** module:
```sh
pip install wat
```
```python
import wat
```
This package has no external dependencies.

## Usage & modifiers
`wat` can quickly inspect things
by using the division operator (for faster typing without parentheses). 
A short syntax `wat / foo` is equivalent to `wat(foo)`.

You can call `wat.modifier / foo` with the following **modifiers**:

- `.short` or `.s` to hide the attributes (variables and methods inside the object)
  and print only value, type, parent types, signature and documentation
- `.dunder` to display dunder attributes (starting with double underscore)
- `.code` to reveal the source code of a function, method, or class
- `.long` to show non-abbreviated values and docstrings
- `.nodocs` to hide documentation for functions and classes
- `.caller` to show how and where the inspection was called (works in files, not REPL)
- `.all` to include all available information
- `.ret` to return the object back after the inspection
- `.str` to return the output string instead of printing it
- `.gray` to disable colorful output in the console
- `.color` to enforce colorful outputs in the console

You can chain modifiers, e.g. `wat.short.str.gray / 'foo'`.

Call `wat.locals` or `wat()` to inspect local variables.  
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
