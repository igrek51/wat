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
