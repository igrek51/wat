from dataclasses import dataclass
import inspect as std_inspect
import os
import re
import sys
from typing import Any, Dict, List, Optional, Type, Iterable, Union


@dataclass
class InspectConfig:
    short: bool
    dunder: bool
    nodocs: bool
    long: bool
    code: bool


@dataclass
class InspectAttribute:
    name: str
    value: Any
    type: Type
    callable: bool
    dunder: bool
    private: bool
    signature: Optional[str]
    doc: Optional[str]


def inspect(
    obj: Any,
    *,
    short: bool = False,
    dunder: bool = False,
    nodocs: bool = False,
    long: bool = False,
    code: bool = False,
    all: bool = False,
):
    print(inspect_format(
        obj, short=short, dunder=dunder or all, long=long or all, nodocs=nodocs, code=code or all
    ))


def inspect_format(
    obj: Any,
    *,
    short: bool = False,
    dunder: bool = False,
    nodocs: bool = False,
    long: bool = False,
    code: bool = False,
) -> str:
    config = InspectConfig(short=short, dunder=dunder, nodocs=nodocs, long=long, code=code)
    output: List[str] = []

    str_value = _format_value(obj)
    repr_value: str = repr(obj)
    if repr_value == str(obj) or repr_value == _strip_color(str_value):
        output.append(f'{STYLE_BRIGHT_BLUE}value:{RESET} {str_value}')
    else:
        output.append(f'{STYLE_BRIGHT_BLUE}str:{RESET} {str_value}')
        output.append(f'{STYLE_BRIGHT_BLUE}repr:{RESET} {STYLE_BRIGHT}{repr_value}{RESET}')

    str_type = _format_type(type(obj))
    output.append(f'{STYLE_BRIGHT_BLUE}type:{RESET} {str_type}')
    parents = _format_parent_types(obj)
    if parents:
        output.append(f'{STYLE_BRIGHT_BLUE}parents:{RESET} {parents}')


    if isinstance(obj, (list, dict, str, bytes, bytearray, tuple, set, frozenset, range)):
        output.append(f'{STYLE_BRIGHT_BLUE}len:{RESET} {_format_value(len(obj))}')
 
    if callable(obj):
        name = getattr(obj, '__name__', '…')
        signature = _get_callable_signature(name, obj)
        output.append(f'{STYLE_BRIGHT_BLUE}signature:{RESET} {signature}')

    doc = _get_doc(obj, long=True)
    if doc and not config.nodocs and callable(obj):
        if doc.count('\n') == 0:
            output.append(f'{STYLE_GRAY}"""{doc}"""{RESET}')
        else:
            output.extend([f'{STYLE_GRAY}"""', doc, f'"""{RESET}'])

    if config.code and (std_inspect.isclass(obj) or callable(obj)):
        source = _get_source_code(obj)
        if source:
            output.append(f'{STYLE_BRIGHT_BLUE}source code:{RESET}\n{source}')

    if not config.short:
        attributes = sorted(_iter_attributes(obj, config), key=lambda attr: attr.name)
        output.extend(_render_attrs_section(attributes, config))

    if sys.stdout.isatty():  # horizontal bar
        terminal_width = os.get_terminal_size().columns
        output.insert(0, STYLE_BLUE + '─' * terminal_width + RESET)
        output.append(STYLE_BLUE + '─' * terminal_width + RESET)

    text = '\n'.join(line for line in output if line is not None)
    if not sys.stdout.isatty():
        text = _strip_color(text)
    return text


def _iter_attributes(obj: Any, config: InspectConfig) -> Iterable[InspectAttribute]:
    keys = dir(obj)
    for key in keys:
        dunder = key.startswith('__') and key.endswith('__')
        if dunder and not config.dunder:
            continue
        private = key.startswith('_') and not dunder
        value = _get_attribute_value(obj, key)
        callable_ = callable(value)
        signature = _get_callable_signature(key, value) if callable_ else None
        doc = _get_doc(value, long=config.long) if callable_ else None
        yield InspectAttribute(
            name=key,
            value=value,
            type=type(value),
            callable=callable_,
            dunder=dunder,
            private=private,
            signature=signature,
            doc=doc,
        )


def _get_attribute_value(obj: Any, key: str) -> Any:
    try:
        return getattr(obj, key)
    except BaseException as e:
        return e


def _get_callable_signature(name: str, obj: Any) -> Optional[str]:
    try:
        _signature = str(std_inspect.signature(obj))
    except (ValueError, TypeError):
        _signature = "(…)"
    
    if std_inspect.isclass(obj):
        prefix = "class "
    elif std_inspect.iscoroutinefunction(obj):
        prefix = "async def "
    elif std_inspect.isfunction(obj):
        prefix = "def "
    elif std_inspect.ismethod(obj):
        prefix = "def "
    elif std_inspect.isbuiltin(obj):
        prefix = "def "
    elif hasattr(obj, '__name__'):
        prefix = "def "
    else:
        prefix = ""
    return f'{STYLE_BLUE}{prefix}{STYLE_BRIGHT_GREEN}{name}{STYLE_GREEN}{_signature}{RESET}'


def _get_source_code(obj: Any) -> Optional[str]:
    try:
        return std_inspect.getsource(obj)
    except (OSError, TypeError, IndentationError) as e:
        return f'failed to get source code: {type(e)}: {e}'


def _get_doc(obj: Any, long: bool) -> Optional[str]:
    doc = std_inspect.getdoc(obj)
    if doc is None:
        return None
    doc = doc.strip()
    if long:
        return doc
    else:
        return _shorten_string(doc)


def _render_attr_variable(attr: InspectAttribute, config: InspectConfig) -> str:
    value_str = _format_short_value(attr.value, long=config.long)
    type_str = _format_type(attr.type)
    return f'  {STYLE_BRIGHT_YELLOW}{attr.name}{STYLE_YELLOW}: {type_str} = {value_str}'


def _render_attr_method(attr: InspectAttribute) -> str:
    if not attr.signature:
        return f'  {attr.name}(…)'
    if attr.doc:
        if attr.doc.count('\n') == 0:
            return f'  {attr.signature} {STYLE_GRAY}# {attr.doc}{RESET}'
        else:
            return f'  {attr.signature}:\n{STYLE_GRAY}"""\n{attr.doc}\n"""{RESET}'
    else:
        return f'  {attr.signature}'


def _format_short_value(value: Any, long: bool) -> str:
    value_str = _format_value(value)
    if long:
        return value_str
    return _shorten_string(value_str)


def _format_value(value: Any, indent: int = 0) -> str:
    if isinstance(value, str):
        return f"{STYLE_GREEN}'{value}'{RESET}"
    if value is None:
        return f'{STYLE_MAGENTA}None{RESET}'
    if value is True:
        return f'{STYLE_BRIGHT_GREEN}True{RESET}'
    if value is False:
        return f'{STYLE_BRIGHT_RED}False{RESET}'
    if isinstance(value, (int, float)):
        return f'{STYLE_RED}{value}{RESET}'
    if isinstance(value, dict):
        return _format_dict_value(value, indent=indent+1)
    if isinstance(value, list):
        return _format_list_value(value, indent=indent+1)
    return f"{STYLE_GREEN}{str(value)}{RESET}"


def _format_dict_value(dic: Dict, indent: int) -> str:
    lines: List[str] = []
    indentation = '    ' * indent
    for key, value in dic.items():
        key_str = _format_value(key, indent)
        value_str = _format_value(value, indent)
        lines.append(f'{indentation}{key_str}: {value_str},')
    if lines:
        small_indent = "    " * (indent-1)
        middle_lines = '\n'.join(lines)
        return f'{STYLE_YELLOW}{{{RESET}\n{middle_lines}\n{small_indent}{STYLE_YELLOW}}}{RESET}'
    else:
        return f'{STYLE_YELLOW}{{}}{RESET}'


def _format_list_value(lst: List, indent: int) -> str:
    lines: List[str] = []
    for value in lst:
        value_str = _format_value(value, indent)
        lines.append('    ' * indent + f'{value_str},')
    if lines:
        small_indent = "    " * (indent-1)
        middle_lines = '\n'.join(lines)
        return f'{STYLE_YELLOW}[{RESET}\n{middle_lines}\n{small_indent}{STYLE_YELLOW}]{RESET}'
    else:
        return f'{STYLE_YELLOW}[]{RESET}'


def _format_type(type_: Type) -> str:
    module = type_.__module__
    if module is None or module == str.__class__.__module__:  # built-in type
        return f'{STYLE_YELLOW}{type_.__name__}{RESET}'
    return f'{STYLE_YELLOW}{module}.{type_.__name__}{RESET}'


def _get_parent_types(type_: Type) -> Iterable[str]:
    if hasattr(type_, '__mro__'):
        for index, base_type in enumerate(type_.__mro__):
            if index == 0:
                continue
            if base_type is object:
                continue
            yield _format_type(base_type)


def _format_parent_types(obj: Any) -> str:
    return ', '.join(_get_parent_types(type(obj)))


def _shorten_string(text: str) -> str:
    first_line, _, rest = text.partition('\n')
    if rest:
        first_line = first_line + '…'
    if len(first_line) > 100:
        first_line = first_line[:100] + '…'
    return first_line + RESET


def _render_attrs_section(attributes: List[InspectAttribute], config: InspectConfig) -> Iterable[str]:
    public_attrs = [attr for attr in attributes if not attr.private and not attr.dunder]
    private_attrs = [attr for attr in attributes if attr.private]
    dunder_attrs = [attr for attr in attributes if attr.dunder]

    public_vars = [attr for attr in public_attrs if not attr.callable]
    private_vars = [attr for attr in private_attrs if not attr.callable]
    dunder_vars = [attr for attr in dunder_attrs if not attr.callable]
    public_methods = [attr for attr in public_attrs if attr.callable]
    private_methods = [attr for attr in private_attrs if attr.callable]
    dunder_methods = [attr for attr in dunder_attrs if attr.callable]

    if public_vars or public_methods:
        yield ""
        yield f"{STYLE_BRIGHT}Public attributes:{RESET}"
        for attr in public_vars:
            yield _render_attr_variable(attr, config)
        if public_vars and public_methods:
            yield ""
        for attr in public_methods:
            yield _render_attr_method(attr)
    
    if private_vars or private_methods:
        yield ""
        yield f"{STYLE_BRIGHT}Private attributes:{RESET}"
        for attr in private_vars:
            yield _render_attr_variable(attr, config)
        if private_vars and private_methods:
            yield ""
        for attr in private_methods:
            yield _render_attr_method(attr)

    if config.dunder and dunder_attrs:
        yield ""
        yield f"{STYLE_BRIGHT}Dunder attributes:{RESET}"
        for attr in dunder_vars:
            yield _render_attr_variable(attr, config)
        if dunder_vars and dunder_methods:
            yield ""
        for attr in dunder_methods:
            yield _render_attr_method(attr)


class Wat:
    """Inspector instance to examine unknown objects with short operators"""
    def __init__(self, **inspect_kwargs):
        self._inspect_kwargs: Dict[str, bool] = inspect_kwargs
        self._config = {}

    def __repr__(self) -> str:
        self._print_help()
        return ''
        
    def __str__(self) -> str:
        return '<Wat Inspector object>'
    
    def _print_help(self):
        text = f"""
Try {STYLE_YELLOW}wat / object{RESET} or {STYLE_YELLOW}wat.modifiers / object{RESET} to inspect an {STYLE_YELLOW}object{RESET}. {STYLE_BRIGHT}Modifiers{RESET} are:
  {STYLE_GREEN}.short{RESET} or {STYLE_GREEN}.s{RESET} to hide attributes (variables and methods)
  {STYLE_GREEN}.long{RESET} to print non-abbreviated values and documentation
  {STYLE_GREEN}.dunder{RESET} to print dunder attributes
  {STYLE_GREEN}.code{RESET} to print source code of a function, method or class
  {STYLE_GREEN}.nodocs{RESET} to hide documentation for functions and classes
  {STYLE_GREEN}.all{RESET} to include all information
  {STYLE_GREEN}.ret{RESET} to return the inspected {STYLE_YELLOW}object{RESET}
Call {STYLE_YELLOW}wat.locals{RESET} or {STYLE_YELLOW}wat(){RESET} to inspect {STYLE_YELLOW}locals(){RESET} variables.
Call {STYLE_YELLOW}wat.globals{RESET} to inspect {STYLE_YELLOW}globals(){RESET} variables.
""".strip()
        if not sys.stdout.isatty():
            text = _strip_color(text)
        print(text)

    def _react_with(self, other: Any) -> Any:
        inspect(other, **self._inspect_kwargs)
        if self._config.get('ret', False):
            return other
    
    def __call__(self, *args: Any, **kwargs: Any) -> Union['Wat', None]:
        if args:
            inspect_kwargs = self._inspect_kwargs.copy()
            inspect_kwargs.update(kwargs)
            return inspect(*args, **inspect_kwargs)
        elif kwargs:
            return Wat(**kwargs)
        else:
            return inspect(_build_locals_object())
    
    def _clone(self) -> 'Wat':
        new_wat = Wat(**self._inspect_kwargs)
        new_wat._config = self._config.copy()
        return new_wat

    def __truediv__(self, other: Any): return self._react_with(other)  # /
    def __add__(self, other: Any): return self._react_with(other)  # +
    def __lshift__(self, other: Any): return self._react_with(other)  # <<
    def __rshift__(self, other: Any): return self._react_with(other)  # >>
    def __or__(self, other: Any): return self._react_with(other)  # |
    def __ror__(self, other: Any): return self._react_with(other)  # |
    def __lt__(self, other: Any): return self._react_with(other)  # <

    def __getattr__(self, name) -> Union['Wat', None]:
        new_wat = self._clone()
        if name in {'short', 's'}:
            new_wat._inspect_kwargs['short'] = True
        elif name == 'long':
            new_wat._inspect_kwargs['long'] = True
        elif name == 'dunder':
            new_wat._inspect_kwargs['dunder'] = True
        elif name == 'code':
            new_wat._inspect_kwargs['code'] = True
        elif name == 'nodocs':
            new_wat._inspect_kwargs['nodocs'] = True
        elif name == 'all':
            new_wat._inspect_kwargs['all'] = True
        elif name == 'ret':
            new_wat._config['ret'] = True
        elif name == 'locals':
            return inspect(_build_locals_object())
        elif name == 'globals':
            return inspect(_build_globals_object())
        elif name == 'wat':
            return self
        else:
            raise AttributeError
        return new_wat

wat = Wat()


def _strip_color(text: str) -> str:
    return re.sub(r'\x1b\[\d+(;\d+)?m', '', text)


def _build_locals_object():
    o = type('locals', (object,), {})()
    frame = std_inspect.currentframe()
    try:
        for _ in range(2):  # back to caller frame
            if frame is not None:
                frame = frame.f_back
        if frame is not None:
            for key, value in frame.f_locals.items():
                setattr(o, key, value)
    finally:
        del frame
    return o


def _build_globals_object():
    o = type('globals', (object,), {})()
    frame = std_inspect.currentframe()
    try:
        for _ in range(2):
            if frame is not None:
                frame = frame.f_back
        if frame is not None:
            for key, value in frame.f_globals.items():
                setattr(o, key, value)
    finally:
        del frame
    return o


RESET ='\033[0m'
STYLE_BRIGHT = '\033[1m'
STYLE_DIM = '\033[2m'

STYLE_RED = '\033[0;31m'
STYLE_BRIGHT_RED = '\033[1;31m'
STYLE_GREEN = '\033[0;32m'
STYLE_BRIGHT_GREEN = '\033[1;32m'
STYLE_YELLOW = '\033[0;33m'
STYLE_BRIGHT_YELLOW = '\033[1;33m'
STYLE_BLUE = '\033[0;34m'
STYLE_BRIGHT_BLUE = '\033[1;34m'
STYLE_MAGENTA = '\033[0;35m'
STYLE_CYAN = '\033[0;36m'
STYLE_WHITE = '\033[0;37m'
STYLE_GRAY = '\033[2;37m'
