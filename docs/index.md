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
This package has no external dependencies.

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
- `.caller` to show how and where the inspection was called (works in files, not REPL)
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
