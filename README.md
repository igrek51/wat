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
