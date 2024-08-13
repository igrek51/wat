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
This package has no dependencies.

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
