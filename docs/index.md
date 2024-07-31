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
code = b'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'
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
wat.code / wat.__call__
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-code-wat-call.png?raw=true)

### Prettify unreadable collections
Nested dictionaries and lists get nicely formatted, indented output:

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-nested-dict-pretty.png?raw=true)

### Debug with breakpoint
You can use Python's `breakpoint()` keyword to launch an interactive debugger in your program. Attach to the interpreter and inspect things on the spot.

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
wat / _
```

### Inspect WAT itself
```python
wat.dunder / wat
wat.code / wat.__truediv__
```

## Environment variables
- `WAT_COLOR="false"` to disable colorful output in the console.
- `WAT_COLOR="true"` to enforce colorful outputs even in non-tty environment.

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
