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
