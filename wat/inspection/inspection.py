from dataclasses import dataclass
import inspect
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
    caller: bool


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


def inspect_format(
    obj: Any,
    *,
    short: bool = False,
    dunder: bool = False,
    nodocs: bool = False,
    long: bool = False,
    code: bool = False,
    caller: bool = False,
    all: bool = False,
) -> str:
    config = InspectConfig(short=short, dunder=dunder or all, nodocs=nodocs, long=long or all, code=code or all, caller=caller or all)
    output: List[str] = list(_yield_inspect_lines(obj, config))

    if sys.stdout.isatty():  # horizontal bar
        terminal_width = os.get_terminal_size().columns
        output.insert(0, STYLE_BLUE + '─' * terminal_width + RESET)
        output.append(STYLE_BLUE + '─' * terminal_width + RESET)

    return '\n'.join(line for line in output if line is not None)


def _yield_inspect_lines(obj, config: InspectConfig) -> Iterable[str]:
    if config.caller:
        yield from _generate_caller_info()

    str_value = _format_value(obj)
    repr_value: str = repr(obj)
    if repr_value == str(obj) or repr_value == _strip_color(str_value):
        yield f'{STYLE_BRIGHT_BLUE}value:{RESET} {str_value}'
    else:
        yield f'{STYLE_BRIGHT_BLUE}str:{RESET} {str_value}'
        yield f'{STYLE_BRIGHT_BLUE}repr:{RESET} {STYLE_BRIGHT}{repr_value}{RESET}'

    str_type = _format_type(type(obj))
    yield f'{STYLE_BRIGHT_BLUE}type:{RESET} {str_type}'
    parents = ', '.join(_get_parent_types(type(obj)))
    if parents:
        yield f'{STYLE_BRIGHT_BLUE}parents:{RESET} {parents}'

    if callable(getattr(obj, '__len__', None)):
        try:
            yield f'{STYLE_BRIGHT_BLUE}len:{RESET} {_format_value(len(obj))}'
        except TypeError:
            pass
 
    if callable(obj):
        name = getattr(obj, '__name__', '…')
        signature = _get_callable_signature(name, obj)
        yield f'{STYLE_BRIGHT_BLUE}signature:{RESET} {signature}'

    doc = _get_doc(obj, long=True)
    if doc and not config.nodocs and callable(obj):
        if doc.count('\n') == 0:
            yield f'{STYLE_GRAY}"""{doc}"""{RESET}'
        else:
            yield from [f'{STYLE_GRAY}"""', doc, f'"""{RESET}']

    if config.code and (inspect.isclass(obj) or callable(obj)):
        source = _get_source_code(obj)
        if source:
            yield f'{STYLE_BRIGHT_BLUE}source code:{RESET}\n{source}'

    if not config.short:
        attributes = sorted(_iter_attributes(obj, config), key=lambda attr: attr.name)
        yield from _render_attrs_section(attributes, config)


def _iter_attributes(obj, config: InspectConfig) -> Iterable[InspectAttribute]:
    for key in dir(obj):
        dunder = key.startswith('__') and key.endswith('__')
        if dunder and not config.dunder:
            continue
        private = key.startswith('_') and not dunder
        try:
            value = getattr(obj, key)
        except BaseException as e:
            value = e
        _callable = callable(value)
        signature = _get_callable_signature(key, value) if _callable else None
        doc = _get_doc(value, long=config.long) if _callable else None
        yield InspectAttribute(
            name=key, value=value, type=type(value), callable=_callable, dunder=dunder,
            private=private, signature=signature, doc=doc,
        )


def _get_callable_signature(name: str, obj) -> Optional[str]:
    try:
        _signature = str(inspect.signature(obj))
    except (ValueError, TypeError):
        _signature = '(…)'
    
    if inspect.isclass(obj):
        prefix = 'class '
    elif inspect.iscoroutinefunction(obj):
        prefix = 'async def '
    elif inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj) or hasattr(obj, '__name__'):
        prefix = 'def '
    else:
        prefix = ''
    return f'{STYLE_BLUE}{prefix}{STYLE_BRIGHT_GREEN}{name}{STYLE_GREEN}{_signature}{RESET}'


def _get_source_code(obj) -> Optional[str]:
    try:
        return inspect.getsource(obj)
    except (OSError, TypeError, IndentationError) as e:
        return f'failed to get source code: {type(e)}: {e}'


def _get_doc(obj, long: bool) -> Optional[str]:
    doc = inspect.getdoc(obj)
    if doc is None:
        return None
    doc = doc.strip()
    return doc if long else _shorten_string(doc)


def _render_attr_variable(attr: InspectAttribute, config: InspectConfig) -> str:
    value_str = _format_short_value(attr.value, long=config.long)
    type_str = _format_type(attr.type)
    return f'  {STYLE_BRIGHT_YELLOW}{attr.name}{STYLE_YELLOW}: {type_str} = {value_str}'


def _render_attr_method(attr: InspectAttribute, config: InspectConfig) -> str:
    if not attr.signature:
        return f'  {attr.name}(…)'
    if attr.doc and not config.nodocs:
        if attr.doc.count('\n') == 0:
            return f'  {attr.signature} {STYLE_GRAY}# {attr.doc}{RESET}'
        else:
            return f'  {attr.signature}:\n{STYLE_GRAY}"""\n{attr.doc}\n"""{RESET}'
    else:
        return f'  {attr.signature}'


def _format_short_value(value, long: bool) -> str:
    value_str = _format_value(value)
    if long:
        return value_str
    return _shorten_string(value_str)


def _format_value(value, indent: int = 0) -> str:
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
    str_val = str(value)
    angle_bracket_match = re.fullmatch(r'<(.*)>', str_val)
    if angle_bracket_match:
        return f'{STYLE_YELLOW}<{STYLE_BRIGHT_YELLOW}{angle_bracket_match.group(1)}{STYLE_YELLOW}>{RESET}'
    return f'{STYLE_GREEN}{str_val}{RESET}'


def _format_dict_value(dic: Dict, indent: int) -> str:
    if indent > 30:
        return f'{STYLE_BRIGHT_RED}ERROR: too deeply nested{RESET}'
    lines: List[str] = []
    indentation = '    ' * indent
    for key, value in dic.items():
        key_str = _format_value(key, indent)
        value_str = _format_value(value, indent)
        lines.append(f'{indentation}{key_str}: {value_str},')
    if lines:
        small_indent = '    ' * (indent-1)
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
        small_indent = '    ' * (indent-1)
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
            if index == 0 or base_type is object:
                continue
            yield _format_type(base_type)


def _generate_caller_info() -> Iterable[str]:
    frame = _caller_stack_frame(6)
    if frame:
        frameinfo = inspect.getframeinfo(frame)
        if frameinfo.filename:
            yield f'{STYLE_BRIGHT_BLUE}caller file: {STYLE_YELLOW}{frameinfo.filename}:{STYLE_BRIGHT_YELLOW}{frameinfo.lineno}{RESET}'
        if frameinfo.code_context:
            code = '\n'.join(frameinfo.code_context).strip()
            yield f'{STYLE_BRIGHT_BLUE}caller expression:{RESET} {code}'


def _shorten_string(text: str) -> str:
    first_line, _, rest = text.partition('\n')
    if rest:
        first_line = first_line + '…'
    if len(first_line) > 100:
        first_line = first_line[:100] + '…'
    return first_line + RESET


def _render_attrs_section(attributes: List[InspectAttribute], config: InspectConfig) -> Iterable[str]:
    public_vars = [a for a in attributes if not a.private and not a.dunder and not a.callable]
    private_vars = [a for a in attributes if a.private and not a.callable]
    dunder_vars = [a for a in attributes if a.dunder and not a.callable]
    public_methods = [a for a in attributes if not a.private and not a.dunder and a.callable]
    private_methods = [a for a in attributes if a.private and a.callable]
    dunder_methods = [a for a in attributes if a.dunder and a.callable]

    if public_vars or public_methods:
        yield ''
        yield f'{STYLE_BRIGHT}Public attributes:{RESET}'
        for attr in public_vars:
            yield _render_attr_variable(attr, config)
        if public_vars and public_methods:
            yield ''
        for attr in public_methods:
            yield _render_attr_method(attr, config)
    
    if private_vars or private_methods:
        yield ''
        yield f'{STYLE_BRIGHT}Private attributes:{RESET}'
        for attr in private_vars:
            yield _render_attr_variable(attr, config)
        if private_vars and private_methods:
            yield ''
        for attr in private_methods:
            yield _render_attr_method(attr, config)

    if config.dunder and (dunder_vars or dunder_methods):
        yield ''
        yield f'{STYLE_BRIGHT}Dunder attributes:{RESET}'
        for attr in dunder_vars:
            yield _render_attr_variable(attr, config)
        if dunder_vars and dunder_methods:
            yield ''
        for attr in dunder_methods:
            yield _render_attr_method(attr, config)


def _caller_stack_frame(depth: int):
    frame = inspect.currentframe()
    for _ in range(depth):  # back to caller frame
        if frame is not None:
            frame = frame.f_back
    return frame


def _render_variables(variables: Dict[str, Any], title: str) -> Iterable[str]:
    yield f'{STYLE_BRIGHT}{title}:{RESET}'
    for name in sorted(variables.keys()):
        value = variables[name]
        value_str = _format_short_value(value, long=False)
        type_str = _format_type(type(value))
        yield f'  {STYLE_BRIGHT_YELLOW}{name}{STYLE_YELLOW}: {type_str} = {value_str}'


def _strip_color(text: str) -> str:
    return re.sub(r'\x1b\[\d+(;\d+)?m', '', text)


class Wat:
    '''Inspector instance to examine unknown objects with short operators'''
    def __init__(self, **inspect_kwargs):
        self._inspect_kwargs = inspect_kwargs
        self._config = {}
        self._inspect_in_progress = False

    def __repr__(self) -> str:
        if not wat._inspect_in_progress:
            self._print_help()
        return ''
        
    def __str__(self) -> str:
        return '<WAT Inspector object>'
    
    def _print_help(self):
        text = f'''Try {STYLE_YELLOW}wat / object{RESET} or {STYLE_YELLOW}wat.modifiers / object{RESET} to inspect an {STYLE_YELLOW}object{RESET}. {STYLE_BRIGHT}Modifiers{RESET} are:
  {STYLE_GREEN}.short{RESET} or {STYLE_GREEN}.s{RESET} to hide attributes (variables and methods)
  {STYLE_GREEN}.dunder{RESET} to print dunder attributes
  {STYLE_GREEN}.code{RESET} to print source code of a function, method or class
  {STYLE_GREEN}.long{RESET} to print non-abbreviated values and documentation
  {STYLE_GREEN}.nodocs{RESET} to hide documentation for functions and classes
  {STYLE_GREEN}.caller{RESET} to show how and where the inspection was called
  {STYLE_GREEN}.all{RESET} to include all information
  {STYLE_GREEN}.ret{RESET} to return the inspected {STYLE_YELLOW}object{RESET}
  {STYLE_GREEN}.str{RESET} to return the output string instead of printing
  {STYLE_GREEN}.gray{RESET} to disable colorful output in the console
  {STYLE_GREEN}.color{RESET} to enforce colorful outputs in the console
Call {STYLE_YELLOW}wat.locals{RESET} or {STYLE_YELLOW}wat(){RESET} to inspect local variables.
Call {STYLE_YELLOW}wat.globals{RESET} to inspect global variables.'''
        if not self._color_enabled():
            text = _strip_color(text)
        print(text)
    
    def __call__(self, *args, **kwargs):
        if args:
            return self.copy(**kwargs).inspect(*args)
        elif kwargs:
            return self.copy(**kwargs)
        else:
            frame = _caller_stack_frame(2)
            local_vars = frame.f_locals if frame else {}
            return self._print_variables(local_vars, 'Local variables')
    
    def inspect(self, other):
        wat._inspect_in_progress = True
        try:
            output = inspect_format(other, **self._inspect_kwargs)
            output_return = self._display_output(output)
            if output_return:
                return output_return
            if self._config.get('ret', False):
                return other
            return None
        finally:
            wat._inspect_in_progress = False
    
    def copy(self, **kwargs) -> 'Wat':
        new_config = self._config.copy()
        for name in kwargs.copy():
            if name in {'ret', 'str', 'gray', 'color'}:
                new_config[name] = kwargs.pop(name)
        new_inspect_kwargs = self._inspect_kwargs.copy()
        new_inspect_kwargs.update(kwargs)
        new_wat = Wat(**new_inspect_kwargs)
        new_wat._config = new_config
        return new_wat
    
    def _display_output(self, output: str) -> Optional[str]:
        if not self._color_enabled():
            output = _strip_color(output)
        if self._config.get('str', False):
            return output
        print(output)
        return None
    
    def _color_enabled(self) -> bool:
        if self._config.get('color', False):
            return True
        if self._config.get('gray', False):
            return False
        env_color = {
            'false': False,
            'true': True,
        }.get(os.environ.get('WAT_COLOR', '').lower())
        if env_color is not None:
            return env_color
        return sys.stdout.isatty()

    def _print_variables(self, variables: Dict[str, Any], title: str) -> Optional[str]:
        lines = list(_render_variables(variables, title))
        output = '\n'.join(line for line in lines if line is not None)
        return self._display_output(output)

    def __truediv__(self, other): return self.inspect(other)  # /
    def __add__(self, other): return self.inspect(other)  # +
    def __lshift__(self, other): return self.inspect(other)  # <<
    def __rshift__(self, other): return self.inspect(other)  # >>
    def __or__(self, other): return self.inspect(other)  # wat |
    def __ror__(self, other): return self.inspect(other)  # | wat
    def __lt__(self, other): return self.inspect(other)  # <

    def __getattr__(self, name) -> Union['Wat', str, None]:
        new_wat = self.copy() 
        if name in {'short', 's'}:
            new_wat._inspect_kwargs['short'] = True
        elif name in {'long', 'dunder', 'code', 'nodocs', 'caller', 'all'}:
            new_wat._inspect_kwargs[name] = True
        elif name in {'ret', 'str', 'gray', 'color'}:
            new_wat._config[name] = True
        elif name == 'locals':
            frame = _caller_stack_frame(2)
            local_vars = frame.f_locals if frame else {}
            return self._print_variables(local_vars, 'Local variables')
        elif name == 'globals':
            frame = _caller_stack_frame(2)
            global_vars = frame.f_globals if frame else {}
            return self._print_variables(global_vars, 'Global variables')
        elif name == 'wat':
            return self
        else:
            raise AttributeError
        return new_wat


RESET = '\033[0m'
STYLE_BRIGHT = '\033[1m'
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
STYLE_GRAY = '\033[2;37m'

wat = Wat()
