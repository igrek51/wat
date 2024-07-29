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
