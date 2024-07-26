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

> [!Warning]
> Before executing Insta-Load snippet, it's recommended to verify what you're about to run.
> If you feel uncomfortable, you can either:
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
A short, no-parentheses syntax `wat / object` is equivalent to `wat(object)`.

You can call `wat.modifiers / object` (or `wat.modifiers(object)`)
with the following **modifiers**:

- `.short` or `.s` to hide attributes (variables and methods)
- `.long` to show non-abbreviated values and documentation
- `.dunder` to display dunder attributes
- `.code` to reveal the source code of a function, method, or class
- `.nodocs` to hide documentation for functions and classes
- `.all` to include all available information

You can chain modifiers, e.g. `wat.long.dunder.nodocs / object`.

Call `wat.locals` or `wat()` to inspect `locals()` variables.
Call `wat.globals` to inspect `globals()` variables.

Type `wat` in the interpreter to learn more about this object itself.

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

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-intro-set.png?raw=true)

Now that you've identified the actual type,
you can put the type annotations in your code to reduce the confusion.

### Look up methods
Listing methods, functions and looking up their signature is extremely beneficial to see how to use them.
Plus, you can read their docstrings.

```python
wat / 'stringy'
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-string.png?raw=true)

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
