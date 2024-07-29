---
hide:
  - navigation
---

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

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-datetime.png?raw=true)

<video width="100%" controls="true" allowFullscreen="true" src="https://github.com/user-attachments/assets/022ef89a-9e35-45be-9e2f-08d2c6af9075" poster="https://raw.githubusercontent.com/igrek51/wat/master/docs/img/wat-intro-set.png">
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

!!! warning
    Before executing Insta-Load snippet, it's recommended to verify what you're about to run.
    If you feel uncomfortable, you can either:

    - Verify what's inside the extracted code beforehand:
      ```python
      print(zlib.decompress(base64.b64decode(code)).decode())
      ```
    - Paste the content of [inspection.py](https://github.com/igrek51/wat/blob/master/wat/inspection/inspection.py) into your interpreter.
      It has the same effect.
    - [Install package with pip](#install-with-pip) and review the code.

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
- `.long` to show non-abbreviated values and documentation
- `.dunder` to display dunder attributes
- `.code` to reveal the source code of a function, method, or class
- `.nodocs` to hide documentation for functions and classes
- `.all` to include all available information
- `.ret` to return the inspected object
- `.str` to return the output string instead of printing

You can chain modifiers, e.g. `wat.long.dunder.nodocs / object`.

Call `wat.locals` or `wat()` to inspect `locals()` variables.  
Call `wat.globals` to inspect `globals()` variables.

Type `wat` in the interpreter to learn more about this object itself.

There are several alternative syntaxes that are equivalent.
Choose the one that works best for you:
```python
wat.short / 'foo'  # fast typing
wat.short('foo')
wat('foo', short=True)  # natural Python syntax
'foo' | wat.short  # similar to piping in Unix
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
you can put the type annotations in your code to reduce the confusion.

### Look up methods
Listing methods, functions and looking up their signature is extremely beneficial to see how to use them.
Plus, you can read their docstrings.

```python
wat / 'stringy'
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-string.png?raw=true)

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-intro-set.png?raw=true)

Use `wat.long` if you want to see full doscstrings.

### Discover function's signature
See the docstrings and the signature of a function or a method to see how to use it.

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
One of the use cases is to explore modules.
For instance you can list functions, classes and the sub-modules of a selected module.

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

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-dict-dunder.png?raw=true)

### Review the code
Look up the source code of a function to see how it really works.

```python
import re
wat.code / re.match
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-code-rematch.png?raw=true)

### Debug with breakpoint
You can use Python's `breakpoint()` keyword to launch an interactive debugger in your program:

```python
logger.debug('init')
x = {'what is it?'}
breakpoint()
logger.debug('done')
```

```python
(Pdb) import wat  # or paste insta-load snippet
(Pdb) wat / x  # inspect local variable
...
(Pdb) c  # continue execution
```

### Explore Python built-ins
```python
wat / __builtins__
```

### Look up local variables
```python
wat()
# or
wat.locals
```

### Look up global variables
```python
wat.globals
```

## Environment variables
- `WAT_COLOR="false"` to disable colorful output in the console.
- `WAT_COLOR="true"` to enforce colorful outputs even in non-tty environment.
