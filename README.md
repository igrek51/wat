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
