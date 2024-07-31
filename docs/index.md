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
