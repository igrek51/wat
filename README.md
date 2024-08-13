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
