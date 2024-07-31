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
