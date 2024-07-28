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
