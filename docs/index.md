---
hide:
  - navigation
---

# 🙀 WAT

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

If you find yourself deep in the Python console, feeling lost and confused,
and wondering "WAT? What is this thing?",
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
A short syntax `wat / foo` is equivalent to `wat(foo)`.

You can call `wat.modifiers / foo` with the following **modifiers**:

- `.short` or `.s` to hide the attributes (variables and methods inside the object)
- `.dunder` to display dunder attributes (starting with `__`)
- `.code` to reveal the source code of a function, method, or class
- `.long` to show non-abbreviated values and docstrings
- `.nodocs` to hide documentation for functions and classes
- `.all` to include all available information
- `.ret` to return the inspected object
- `.str` to return the output string instead of printing it
- `.gray` to disable colorful output in the console

You can chain modifiers, e.g. `wat.long.dunder.nodocs / foo`.

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

## Use Case Examples

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

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
