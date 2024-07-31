---
hide:
  - navigation
---

# 🙀 WAT Inspector

<div align="center">
    <a href="https://github.com/igrek51/wat">GitHub</a>
    -
    <a href="https://pypi.org/project/wat-inspector">PyPI</a>
    -
    <a href="https://igrek51.github.io/wat">Documentation</a>
</div>

Deep inspection of Python objects.

**WAT** is a powerful inspection tool
that allows you to delve into and examine unknown objects at runtime.

> "Wat" is a variant of the English word "what" that is often used to express confusion or disgust

If you find yourself deep within the Python console, feeling dazed and confused,
wondering "WAT? What's that thing?",
that's where the `wat` inspector comes in handy.

Start the Python Interpreter (or attach to one) and execute `wat / object` on any `object`
to investigate its
**type**, **formatted value**, **variables**, **methods**, **parent types**, **signature**,
**documentation**, and even its **source code**.
Alternatively, you can use `wat(object)` syntax.

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-datetime-now.png?raw=true)

<video width="100%" controls="true" allowFullscreen="true" src="https://github.com/user-attachments/assets/022ef89a-9e35-45be-9e2f-08d2c6af9075" poster="https://raw.githubusercontent.com/igrek51/wat/master/docs/img/wat-set.png">
</video>

## Import

### Insta-Load
If you want to quickly debug something,
you can use this inspector **without installing anything**, in the same session.

Load it on the fly by pasting this snippet to your Python interpreter:
```python
import base64, zlib
code = b'eJzdW+tu20YW/p+nILw/RDqs1m72AqhVdt3ETQOkzcJ1Nwgcg6DEkc2GIgWSiu0VBPQh9hn2wfZJ9lzmTlKSmy6wWAOWyJlzvplzmTNnLlrU1TLI0jadF2nTiCbIl6uqbk3RE1mQl81KzNsgbYKmzRL5qmorTVcL9dQ8NE8WCN8+rPLyRiGflQ9x8DKft3HwJm/g8+2qzasyLeLg8mEl4uB1K+p0VsDTTyVUPPmr6Qt9Bq+57RdVuchvJk8C+GtuAXoSzKqqoPdsXWaitgrKKqvmjVVQVOWN9TqvMiFfh9o7a9s6n61bwU2W6RI4mramt09psYZXEI5eQWR4Q3kYPS0KFGlXD1d1/iltbZImvynTdl1DmdLRFbR3zfzV3C/OxEKZKVlU9TJtQyKtZj9Tz2J6O459jQXT4Nu0aETc6ZhbY+vQrTHKdMuNVt1yUIdfHAVfPEdtTiQj2hZqHVuH1Okpfcayo1P+CqoaUWPZySl/xdSzKX5oAuzTFD9kScQ6WrerNegDXZK0CW1fsabhLSHzQpHUK7+HoFjmrsVK0pBHACGWmPp8YZEE0ykSUS32wa1JoCpfJfOqqOpQNx2xWkxPx+lqJcosXIw2P16+f3OefHPx+tV3l8k3b34633JPNhfnP55fboONRtmOuDsCNP4oQLTLMNyBICinQbHrtxujg62kkNjYGA4mS/f4GtIHatA2387maUg6QmCJameV1qJsG6sZLiGixrGkJH2UAhWPbl8WqOYBVsWI8Ea0acv+EQejJClEmSSjOPihKkX0OEcAVtOk67tQxfrr6wJWmIYw0oFi/H5hMXVs9O9f/mW5gg5bqExgShRsomtC5I0DrdVD3VAHRGNHVaTEgGGv2oVH7iwFgcsahpGSFKnSMoNo0cpYM+aIQaUDemC+8bxal204+lCOIhywJ4ZghxivLs7eb4+OjjaAQN+Ol3cHpQUl7luEuupggeoBLQ4WIwvw2liT5aJQh1KF1rw9zhua23QQckS2ZG6qdT3XluS3BCFDx3jQHNcdpAzHptwAzRRShg/lhkst17QMxTOXbidV0zIO3gaqRBYmOeQQialhN2D+KA4+iodpkS5nWUrcE/oco0923FEqP4HRmknIJmlAgzDvhqYBDa47DNnPGBQOMKBrIHwII7ICR/ZElKjtLLRUDV1e5jCZJ3d51t6CMFUzRqXr8ib/hwgjMGixXpaN31OwrKjb8CQOpJJBu8FTGJz//GUUHPvoTwPS9dDwezREC4qCLuOoGP9c5WVY5KUIIOIE9JCXsgFUDZc0ZFMKaraRd+mHmnAmSCxTUzBEgZKIKBHqcwHOgqSpJm5uQfmHSj2v/JTvmrsBjoNeluXW3I4yQjmKiNWmvzIxmWIxuEJat81d3t6GEDpH7AtYAdq2ip1Yw/xemJLpmTPMoKrNy7XQhTKX7GtbNo2IDKWZdI6DTqcVZ1IdGjemhzqqA4uOHpysPGoqANCY247sOSihgEj+YTTqxnZiktFdagef98I85KLIOll96KgUg8EUu+aUUotTbtepwCxhSjkJS+LWqs5Mda/ceieTdaukJafy263USpzqJw+4mk9xitCFEY+NAQvL8QFiUxpLQwJK2Nna+sF4nRxtTkqgvUPcz8WqDb5JG3FOjxArcd0oOvzCdGcgSaCOxHoJQ11yVj09nUtst8NM2574DLzJHmWHw7+jIs7ruqp5LUqP0QDwUQhpT3Sk4/3A5DqxBqVY5PfIycvKI5mLd5mrGoIlBMnFuuSJZggobR7KeYA6HATbi7GTeyna2yr7dbyzdV6AFIcy36ZNX3q5l9XOmgzFkT0pmMQDM44NU23dZOTVxfn5D9sNtrrVeRYVGavrtYlxWy8jOtxJZddslQEew5nJRXnm2x99t4whgGWwhEixGXbU/jG2GC3SHKbSoK1wvAZ2whVsKGaJaAuPwpZL5s4yIpj1/ZBsHJo9aSSIk3XDvI/BuNNNHaEZCRNtmuhDzU2d8NmArscPZGVCqSIsnxCpvAmBWAZAK52D8FfnNHlxLujPC7vyBb1fQSE04aW/WmdR4zK4UoI5NF/pHSMPgGxDnPgUuR4duEvo5P35mzdv3203OpVVXiwrpK2xiS20sdE9Vla3VSKHfb9CXMll2kbNmvVZ1wmhv6ZrFDpHip/KcT/Lzn5U4Z7lVgffDNbAXi79Tlbj8kuPYgXSXXrtgJ3A8sRdh0GBxv5QWmuxYc/sA5Z26PEes7nYGYo7PdDi3j2KNLPtY/7o0USR09FuF3MKTBP4xnz9pOMveQMxok3LuVApHIJ2dXTkxOHRRm46Se3qmZfz1qG4omP/92evzn+4PNsilWMgGwI3CYYhnKkCSQdxaFNzL9DF+cstUfo4XQ2FoExY6RdV2kY9qlLAiLhx99GGMbN83naxlF2x1jausuuUv56eRsPIRd7sQMbaA5DlPqPM4SwvTssbyBNndTr/CDMVIM5vacd1vFgXBb2G9ejrcHwcPR/FCkb3tod7WJ8yeH49EGu7UOMbyN1W4Wnkhd/njjn8ZmSmIbvqpRlde8DjRB6hWGOtO86oLngePDs5yBXPLy7eXkwgT6ggpRSr4iEoRdOKzOk6Lt6b3n3y3OQjuBOARbhrwMX2UjlW46REFxzDQn3Z2At9IOkNZMTKcGaJuSfudRlIAGtLyur2diObxtnSTJCx2YZi6c36dgmrlkTqGbJOLDsCmUMu+uLUNLvMswychQA6GyVNtM8DNxuzOWZD0WaZ1QvP7bbbQ+Yiv6ltvwda47Zo5FnJDg8c9hT0A+0CCPUbWdPzueApyva/ZcerX2XG68db8eq614b68CTh40nXZMsqWxe4uCWKcZJwQZIovUkCOdnixrFioSgNHLS2TWze/Q6nWuMl33ZnqFQ8jL4dDzLrpYxzkOOLrnf8zFLGWosSNa1Gl3XlLkbRh9FW93EwSxvBh1TgzqJcLwGylVoeS9bIzS9ldL7vyWjxr7OhJ3mslhrcE4G0/EBm3vNyvECDufmcf+5llrTaTaRN8OiHfb9fz7zDItG9ZBL3ac0mk0Ze5HXT0pCIA1B8DfMPeiMQjwG+zWkng9YCylRIYllF8wOb9fKUD6n08BdlaGojmCJPT072olxNgOrawVLeabdEDthZU/WdGsjg2NlsPmiL2jjsaj0r8jm3gkEWH8g/6QF80joisZdrapdY7QfzIoY2ITlOS4KDkW1UeUthbRRwKIDTAxYNluj97I7otmxqO9EVZBjHkXQYSMoziOPIu6M/3G1eZh8m2Q6pdsL4gg0LtQvGl6sHBU/GLWsBsyulGV4ci+QWnSnQ6z15KeBvxG55yMRZ+akg7CkMG5/0hb7BLR99dmdvP9ii4PgYkqVXnp5u7WAc2nkxFw5s70W9unZ/vGLVuD9Us1b7v4VqbXFIt0Py7Ffufs692nXO1ag/trM/WrkvJc6BurUCym+gWjs8WZI8XrH7GYf1yqcb71I5LR8dHclZjDIm3ijAzWhxny5xxlyXH8vqrpT5TBPgQSVfTwuqFaZSVd0cyX7SrAo5ct4mSdiIYhEHx8fqztvHu7S+aezLC0AwTtxqXjhf0akS7qLhssSl8Nj1VbTNdgA4L5NVXd1AJtKo+2xWZ+lqE3fWzXWkzXCKuEvbXjhX8dwq+DxkWbeiUFvj+KcyspHVMO4mDLWr6L9+d3YZGPOwCZ5bKFZrhNQ5jl+gaS7rh8DNz0Gi4PcST13WgQY6RGPI4/NFLsBhfXJwEX3ptPQ4Hcqxd5vsewWpkFLekXY2W/gaSbdrqtbqxW2e2cEyCNVA5EEmB0nUaQG3Wi0YUiWYu/winc1q8SmHyJXxileO1moOawe5F9FB4yHZwcv8eNNhxJOeDpt1ChRUMJ8H6pwwlvLQpSC6BOvj8UUpXz9O5ymWKER5p4rvF3fQIIdwDD4v1qjtooBnXpH0KQP81+JSdz9uhfIYUOwOh+n6Qlv3w8lLK7xooegl0gwVRlqEsg7UTZ0+WFhZ3qCnBHRdZbEu9DUYxofg0lSFePICBe4OjqKCHKvZNX7CqGe4uFQMYgi1946Hmr0pqpnV7iCypOuFhrDgHOBZ0W74io8VVwau+eAf6d4q43CH2aiZFDjU03HE8bGK/GohS/fKr0YwRclrlTHfMoD6a/cQCtncRbgzVeDedM8cA0Nu9WDJ3WUcr1cZ7hHIKcuhlO4HvQs7c9tYvofHLh+doEsxh8H81gbPveyZRts05A1AcierNIqD0RssM9YfGbuo/rJZKvD52rfDoAGGZkXQOh6+mJnIPlfHPznGzMQub8NT8+gQfUaLeiASqQ9lZhjNqyJ9SLg25C/PzguXt7s/IzEdKh/CTj3wJD0cAR04KyUX0TAmCthnUOf+0wIv8RWeznYo281oyLd1VkGDyLoqLO4SnPqn0uN2K1pSWzmWI7c3iqQoksmMfM8o0tPkfX61w9RzZWFQ1RjCta4x6u4PWtrjnLDl+0dva8AwYFjHUbzo50N3blGY5M0MVVaNfrdTYRx5cdDmbSH2Kk3tfWM40DdjTSv6SeJF/iXT3fdEGX3wmqgl7N4xyRNDC7Eiyz/pucEKQhMHSsUqIrAR0iz7DO6iuc0X7WcA1J8LUNWf0/pncRef0295vVAj0A3t4Qn8ui8OUQscSQInEcEfNYC7bUa0EMC97Ga0dQegjk9uALuSLNf+RESzMP9aAlwc0//RgYBEuwePM/1DESX1HkzM/w9FJNo9eLw2OBRRUu/BhLnqUEAk3YOG8+gAGkflKyLZg4JBew8KkuxBoYlmDwzR7PU0zPBH/8VUrqfvnPs/vlFm9Fp9RYUHNHuX+uazmtyV2KZ5IwJ9xEIXJocyC5PAqLMrbynSc3AlIWoxbtazsB59uD+dfbj6kD0Nv4KP6C9LDDDwz6sWQvUSCoTDDSnGE+UnJsCNJ93R0QLThNHE/i0lleMcB8XoI1y6peSiasYAlNdVybnGu7PL5MXbN28vqDcRrC/vRB2aH62YVq15t3trW1HZkvf83oXF7Pc0lNbNPuQBYM0/NrNvks7XNZ4sUpXMB52UH7OHBGN5nZY3Ivyye9bKqL0yaRDZMH2PF8ksnX98cjiEOgiU3DwifcXJHcRO/p2JgjktjXWHyf+5ymRA+ZU6G85C92a5PSeq/Vv7G2Lcuhv6qEmVS8hfn5ldEPxBUGjf11O/sdEkV8h77dbvuEdsXyHmJYNZBQ9cILZ+lWKIpYCDt4gfeYGYFBJMRx9Onj27OlmOntiglO5jxamuePn6e136pS69OH+pS0++enbq4Tj1p3Y9bb3ZrF/6rC7FqU3B4tncz3xuj+TUIcHfyFnMf/CZHYJTm0DeSLW5/6grX7w/c0T6k655993rS6fJP1uKOHtvFEs1/wHWdcHv'
exec(zlib.decompress(base64.b64decode(code)).decode(), globals())
```

Now you can use `wat` object.

!!! warning
    Before executing Insta-Load snippet, it's recommended to verify what you're about to run.
    You can either:

    - Verify what's inside the extracted code beforehand:
      ```python
      print(zlib.decompress(base64.b64decode(code)).decode())
      ```
    - Paste the content of [inspection.py](https://github.com/igrek51/wat/blob/master/wat/inspection/inspection.py) into your interpreter.
      It has the same effect.
    - [Install package with pip](#install-with-pip) and review the code.

### Install with pip
Alternatively, install **wat-inspector** package and import inspection tool from **wat** module:
```sh
pip install wat-inspector
```
```python
import wat
```

## Usage & modifiers
`wat` object can quickly inspect things
by using the division operator (for faster typing without parentheses). 
A short syntax `wat / object` is equivalent to `wat(object)`.

You can call `wat.modifiers / object` with the following **modifiers**:

- `.short` or `.s` to hide attributes (variables and methods)
- `.dunder` to display dunder attributes
- `.code` to reveal the source code of a function, method, or class
- `.long` to show non-abbreviated values and documentation
- `.nodocs` to hide documentation for functions and classes
- `.all` to include all available information
- `.ret` to return the inspected object
- `.str` to return the output string instead of printing
- `.gray` to disable colorful output in the console

You can chain modifiers, e.g. `wat.long.dunder.nodocs / object`.

Call `wat.locals` or `wat()` to inspect local variables.  
Call `wat.globals` to inspect global variables.

Type `wat` in the interpreter to learn more about this object itself.

There are several alternative syntaxes that are equivalent.
Choose the one that works best for you:
```python
wat.short / 'foo'  # fast typing
wat.short('foo')
wat('foo', short=True)  # natural Python syntax
'foo' | wat.short  # Unix piping
```

## Use Cases Examples

### Determine type
In a dynamic typing language like Python, it's often hard to determine the type of an object. WAT Inspector can help you with that by showing the name of the type with the module it comes from.

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
you can put the type annotations in your code to reduce the confusion.

### Look up methods
By listing out methods and their signatures, you can easily grasp how to use the unknown object.
Plus, you can read their docstrings.

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
One of the use cases is to explore modules.
For instance you can list functions, classes and the sub-modules of a selected module.

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
import re
wat.code / re.match
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-code-rematch.png?raw=true)

### Prettify unreadable collections
```python
import sys
wat.s / sys.modules
```
This will give you a nicely formatted, indented output, even for nested dictionaries or lists.

### Debug with breakpoint
You can use Python's `breakpoint()` keyword to launch an interactive debugger in your program:

```python
logger.debug('init')
x = {'what is it?'}
breakpoint()
logger.debug('done')
```

```python
(Pdb) import wat  # or paste insta-load snippet
(Pdb) wat / x  # inspect local variable
...
(Pdb) c  # continue execution
```

### Look up local and global variables
```python
wat.locals
# Local variables:
#   __annotations__: dict = {}
#   __builtins__: module = <module 'builtins' (built-in)>
#   __doc__: NoneType = None
#   __loader__: type = <class '_frozen_importlib.BuiltinImporter'>
#   __name__: str = '__main__'
#   __package__: NoneType = None
#   __spec__: NoneType = None
#   wat: wat.inspection.inspection.Wat = <WAT Inspector object>

wat.globals
# Global variables:
# ...
```

### Learn Python
With these snippets you can better understand Python internals.

```python
wat.s / reversed([])
# value: <list_reverseiterator object at 0x76749d1cb400>
# type: list_reverseiterator
```

```python
x = (1 << 53) + 1
wat.s / x
# value: 9007199254740993
# type: int
wat.s / (x + 1.0)
# value: 9007199254740992.0
# type: float
```

```python
x = float("nan")
wat.s / {x, x, float(x), float(x), float("nan"), float("nan")}
# value: {nan, nan, nan}
# type: set
# len: 3
```

```python
wat.s / 1 ** -1
# value: 1.0
# type: float
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
# value: Ellipsis
# type: ellipsis
```

### Inspect WAT itself
```python
wat / wat
wat.code / wat.__truediv__
```

## Environment variables
- `WAT_COLOR="false"` to disable colorful output in the console.
- `WAT_COLOR="true"` to enforce colorful outputs even in non-tty environment.

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
