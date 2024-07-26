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
