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

## References
- Inspired by [Rich Inspect](https://github.com/Textualize/rich?tab=readme-ov-file#rich-inspect)
