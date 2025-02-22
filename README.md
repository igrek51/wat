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
