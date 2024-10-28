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
import colorsys
wat.code / colorsys.hsv_to_rgb
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
