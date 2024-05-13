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

Start the Python Interpreter (or attach to your program) and execute `wat(object)` on any `object`
to investigate its
**type**, **formatted value**, **variables**, **methods**, **parent types**, **signature**,
**documentation**, and even its **source code**.

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-intro-set.png?raw=true)

<video width="100%" controls="true" allowFullscreen="true" src="https://github.com/igrek51/wat/assets/12595017/3585123a-c1c4-4ca3-85cd-f52e82e9c744" poster="https://raw.githubusercontent.com/igrek51/wat/master/docs/img/wat-intro-set.png">
</video>

## Import
```sh
pip install wat-inspector
```

Import inspection tool from **wat** package:
```python
from wat import wat
```

Alternatively, use **Insta-Load** in the section below.

### Insta-Load
If you want to debug something quickly,
you don't even need to install anything to use the inspector.

Load it on the fly by pasting this snippet to your Python interpreter:
```python
import base64, zlib
code = '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'
exec(zlib.decompress(base64.b64decode(code.encode())).decode(), globals())
```

Now you can use `wat` object.

## Usage & modifiers
`wat` object can quickly inspect things
by using the division operator (to avoid typing parentheses). 
A short, no-parentheses syntax `wat / object` is equivalent to `wat(object)`.

You can call `wat.modifiers / object` (or `wat.modifiers(object)`)
with the following **modifiers**:

- `.short` to hide attributes (variables and methods)
- `.long` to show non-abbreviated values and documentation
- `.dunder` to display dunder attributes
- `.code` to reveal the source code of a function, method, or class
- `.nodocs` to hide documentation for functions and classes
- `.all` to include all available information

You can chain modifiers, e.g. `wat.long.dunder.nodocs / object`.

Call `wat()` to inspect `locals()` variables.

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

Now that you've identified the actual type, you can put the type annotations in your code to reduce the confusion.

### Look up methods
Listing methods, functions and looking up their signature is extremely beneficial to see how to use them.
Plus, you can read their docstrings.

```python
wat / 'stringy'
```

![](https://github.com/igrek51/wat/blob/master/docs/img/wat-string.png?raw=true)

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
(Pdb) from wat import wat  # or paste insta-load snippet
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
