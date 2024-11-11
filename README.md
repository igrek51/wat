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
Alternatively, install **wat-inspector** package and import inspection tool from **wat** module:
```sh
pip install wat-inspector
```
```python
import wat
```
This package has no external dependencies.

## Usage & modifiers
`wat` can quickly inspect things
by using the division operator (for faster typing without parentheses). 
A short syntax `wat / foo` is equivalent to `wat(foo)`.

You can call `wat.modifiers / foo` with the following **modifiers**:

- `.short` or `.s` to hide the attributes (variables and methods inside the object)
- `.dunder` to display dunder attributes (starting with double underscore)
- `.code` to reveal the source code of a function, method, or class
- `.long` to show non-abbreviated values and docstrings
- `.nodocs` to hide documentation for functions and classes
- `.caller` to show how and where the inspection was called (works in files, not REPL)
- `.all` to include all available information
- `.ret` to return the inspected object
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

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
