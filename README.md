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

<video width="100%" controls="true" allowfullscreen="true" src="https://raw.githubusercontent.com/igrek51/nuclear/master/docs/demo/demo-inspect.mp4" poster="https://raw.githubusercontent.com/igrek51/nuclear/master/docs/demo/demo-inspect-poster.png">
</video>

## Import
Import inspection tools from **wat** package.
```sh
pip install wat-inspector
```
```python
from wat import wat
```

Alternatively, use **Insta-Load** in the section below.

### Insta-Load
If you want to debug something quickly,
you don't even need to install **wat** package to use the inspector.

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
>>> wat.short({None})
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

![](https://github.com/igrek51/nuclear/blob/master/docs/img/wat-string.png?raw=true)

### Discover function's signature
See the docstrings and the signature of a function or a method to see how to use it.

```python
wat / str.split
```

![](https://github.com/igrek51/nuclear/blob/master/docs/img/wat-str-split.png?raw=true)

### Look up attributes
List the attribues and their types to see what's really inside the inspected object.
```python
wat / re.match('(\d)_(.*)', '1_title')
```

![](https://github.com/igrek51/nuclear/blob/master/docs/img/wat-re-match.png?raw=true)

### Explore modules
One of the use cases is to explore modules.
For instance you can list functions, classes and the sub-modules of a selected module.

```python
import pathlib
wat / pathlib
```

![](https://github.com/igrek51/nuclear/blob/master/docs/img/wat-pathlib.png?raw=true)

Then, you can navigate further, e.g. `wat / pathlib.fnmatch`.

### Explore dunder attributes
```python
wat.dunder / {}
```

![](https://github.com/igrek51/nuclear/blob/master/docs/img/wat-dict-dunder.png?raw=true)

### Review the code
Look up the source code of a function to see how it really works.

```python
import re
wat.code / re.match
```

![](https://github.com/igrek51/nuclear/blob/master/docs/img/wat-code-rematch.png?raw=true)

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
