# 🙀 WAT Inspector

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

If you find yourself deep within the Python console, feeling dazed and confused,
wondering "WAT? What's that thing?",
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
A short syntax `wat / object` is equivalent to `wat(object)`.

You can call `wat.modifiers / object` with the following **modifiers**:

- `.short` or `.s` to hide attributes (variables and methods)
- `.dunder` to display dunder attributes
- `.code` to reveal the source code of a function, method, or class
- `.long` to show non-abbreviated values and documentation
- `.nodocs` to hide documentation for functions and classes
- `.all` to include all available information
- `.ret` to return the inspected object
- `.str` to return the output string instead of printing
- `.gray` to disable colorful output in the console

You can chain modifiers, e.g. `wat.long.dunder.nodocs / object`.

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

## Use Cases Examples

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
wat.s / reversed([])
# value: <list_reverseiterator object at 0x76749d1cb400>
# type: list_reverseiterator
```

```python
x = (1 << 53) + 1
wat.s / x
# value: 9007199254740993
# type: int
wat.s / (x + 1.0)
# value: 9007199254740992.0
# type: float
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
wat / _
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
