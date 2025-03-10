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
    private: bool


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
    public: bool = False,
    all: bool = False,
) -> str:
    config = InspectConfig(
        short=short,
        dunder=dunder or all,
        nodocs=nodocs,
        long=long or all,
        code=code or all,
        caller=caller or all,
        private=not public,
    )
    output: List[str] = list(_yield_inspect_lines(obj, config))

    if sys.stdout.isatty():  # horizontal bar
        terminal_width = os.get_terminal_size().columns
        output.insert(0, style.BAR + '─' * terminal_width + RESET)
        output.append(style.BAR + '─' * terminal_width + RESET)

    return '\n'.join(output)


def _yield_inspect_lines(obj, config: InspectConfig) -> Iterable[str]:
    if config.caller:
        yield from _generate_caller_info()

    str_value = _format_value(obj, long=True)
    repr_value: str = repr(obj)
    if repr_value == str(obj) or repr_value == _strip_color(str_value):
        yield f'{style.TRAIT}value:{RESET} {str_value}'
    else:
        yield f'{style.TRAIT}str:{RESET} {str_value}'
        yield f'{style.TRAIT}repr:{RESET} {style.HEAD}{repr_value}{RESET}'

    str_type = _format_type(type(obj))
    yield f'{style.TRAIT}type:{RESET} {str_type}'
    parents = ', '.join(_get_parent_types(type(obj)))
    if parents:
        yield f'{style.TRAIT}parents:{RESET} {parents}'

    if callable(getattr(obj, '__len__', None)):
        try:
            yield f'{style.TRAIT}len:{RESET} {_format_value(len(obj))}'
        except TypeError:
            pass
 
    if callable(obj):
        name = getattr(obj, '__name__', '…')
        signature = _get_callable_signature(name, obj)
        yield f'{style.TRAIT}signature:{RESET} {signature}'

    doc = _get_doc(obj, long=True)
    if doc and not config.nodocs and callable(obj):
        if doc.count('\n') == 0:
            yield f'{style.DOCS}"""{doc}"""{RESET}'
        else:
            yield from [f'{style.DOCS}"""', doc, f'"""{RESET}']

    if config.code and (inspect.isclass(obj) or callable(obj)):
        source = _get_source_code(obj)
        if source:
            yield f'{style.TRAIT}source code:{RESET}\n{source}'

    if not config.short:
        attributes = sorted(_iter_attributes(obj, config), key=lambda attr: attr.name)
        yield from _render_attrs_sections(attributes, config)


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
    return f'{style.KEYWORD}{prefix}{style.CALLABLE}{name}{style.SIGNATURE}{_signature}{RESET}'


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
    value_str = _format_value(attr.value, long=config.long)
    if not config.long:
        value_str = _shorten_string(value_str)
    type_str = _format_type(attr.type)
    return f'  {style.VARIABLE}{attr.name}{style.CODE}: {type_str} = {value_str}'


def _shorten_string(text: str) -> str:
    first_line, _, rest = text.partition('\n')
    if rest or len(_strip_color(first_line)) > 100:
        return first_line[:100] + RESET + '…'
    return first_line


def _render_attr_method(attr: InspectAttribute, config: InspectConfig) -> str:
    if not attr.signature:
        return f'  {attr.name}(…)'
    if attr.doc and not config.nodocs:
        if attr.doc.count('\n') == 0:
            return f'  {attr.signature} {style.DOCS}# {attr.doc}{RESET}'
        else:
            return f'  {attr.signature}:\n{style.DOCS}"""\n{attr.doc}\n"""{RESET}'
    else:
        return f'  {attr.signature}'


def _format_value(value, long: bool = True, indent: int = 0) -> str:
    if isinstance(value, str):
        return f"{style.STR}'{value}'{RESET}"
    if value is None:
        return f'{style.NONE}None{RESET}'
    if value is True:
        return f'{style.TRUE}True{RESET}'
    if value is False:
        return f'{style.FALSE}False{RESET}'
    if isinstance(value, (int, float)):
        return f'{style.NUMBER}{value}{RESET}'
    if isinstance(value, dict):
        return _format_dict_value(value, long, indent+1)
    if isinstance(value, list):
        return _format_list_value(value, long, indent+1)
    str_val = str(value)
    angle_bracket_match = re.fullmatch(r'<(.*)>', str_val)
    if angle_bracket_match:
        return f'{style.CODE}<{style.VARIABLE}{angle_bracket_match.group(1)}{style.CODE}>{RESET}'
    return f'{style.STR}{str_val}{RESET}'


def _format_dict_value(dic: Dict, long: bool, indent: int) -> str:
    if indent > 30:
        return f'{style.FALSE}ERROR: too deeply nested{RESET}'
    if not len(dic):
        return f'{style.CODE}{{}}{RESET}'
    items = (
        f'{_format_value(k, long, indent)}: {_format_value(v, long, indent)}'
        for k, v in dic.items()
    )
    if not long:
        items_str = ', '.join(items)
        return f'{style.CODE}{{{RESET}{items_str}{style.CODE}}}{RESET}'
    lines = '\n'.join('    ' * indent + f'{it},' for it in items)
    end_indent = '    ' * (indent-1)
    return f'{style.CODE}{{{RESET}\n{lines}\n{end_indent}{style.CODE}}}{RESET}'


def _format_list_value(lst: List, long: bool, indent: int) -> str:
    if indent > 30:
        return f'{style.FALSE}ERROR: too deeply nested{RESET}'
    if not len(lst):
        return f'{style.CODE}[]{RESET}'
    items = (_format_value(val, long, indent) for val in lst)
    if not long:
        items_str = ', '.join(items)
        return f'{style.CODE}[{RESET}{items_str}{style.CODE}]{RESET}'
    lines = '\n'.join('    ' * indent + f'{it},' for it in items)
    end_indent = '    ' * (indent-1)
    return f'{style.CODE}[{RESET}\n{lines}\n{end_indent}{style.CODE}]{RESET}'


def _format_type(type_: Type) -> str:
    module = type_.__module__
    if module is None or module == str.__class__.__module__:  # built-in type
        return f'{style.CODE}{type_.__name__}{RESET}'
    return f'{style.CODE}{module}.{type_.__name__}{RESET}'


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
            yield f'{style.TRAIT}caller file: {style.CODE}{frameinfo.filename}:{frameinfo.lineno}{RESET}'
        if frameinfo.code_context:
            code = '\n'.join(frameinfo.code_context).strip()
            yield f'{style.TRAIT}caller expression:{RESET} {code}'


def _render_attrs_sections(attrs: List[InspectAttribute], config: InspectConfig) -> Iterable[str]:
    public_attrs = [a for a in attrs if not a.private and not a.dunder]
    private_attrs = [a for a in attrs if a.private]
    dunder_attrs = [a for a in attrs if a.dunder]
    if public_attrs:
        yield from _render_attrs_section('Public attributes', public_attrs, config)
    if config.private and private_attrs:
        yield from _render_attrs_section('Private attributes', private_attrs, config)
    if config.dunder and dunder_attrs:
        yield from _render_attrs_section('Dunder attributes', dunder_attrs, config)


def _render_attrs_section(title: str, attrs: List[InspectAttribute], config: InspectConfig) -> Iterable[str]:
    attr_vars = [a for a in attrs if not a.callable]
    attr_methods = [a for a in attrs if a.callable]
    yield ''
    yield f'{style.HEAD}{title}:{RESET}'
    for attr in attr_vars:
        yield _render_attr_variable(attr, config)
    if attr_vars and attr_methods:
        yield ''
    for attr in attr_methods:
        yield _render_attr_method(attr, config)


def _caller_stack_frame(depth: int):
    frame = inspect.currentframe()
    for _ in range(depth):  # back to caller frame
        if frame is not None:
            frame = frame.f_back
    return frame


def _render_variables(variables: Dict[str, Any], title: str, long: bool) -> Iterable[str]:
    yield f'{style.HEAD}{title}:{RESET}'
    for name in sorted(variables.keys()):
        value_str = _format_value(variables[name], long)
        type_str = _format_type(type(variables[name]))
        yield f'  {style.VARIABLE}{name}{style.CODE}: {type_str} = {value_str}'


def _strip_color(text: str) -> str:
    return re.sub(r'\x1b\[\d+(;\d+)?m', '', text)


class Wat:
    '''Inspector instance to examine unknown objects'''
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
        text = f'''Try {style.CODE}wat / object{RESET} or {style.CODE}wat.modifiers / object{RESET} to inspect an {style.CODE}object{RESET}. {style.HEAD}Modifiers{RESET} are:
  {style.STR}.short{RESET} or {style.STR}.s{RESET} to hide attributes (variables and methods)
  {style.STR}.dunder{RESET} to print dunder attributes
  {style.STR}.long{RESET} to print non-abbreviated values and documentation
  {style.STR}.code{RESET} to print source code of a function, method or class
  {style.STR}.nodocs{RESET} to hide documentation for functions and classes
  {style.STR}.caller{RESET} to show how and where the inspection was called
  {style.STR}.public{RESET} to show only public attributes
  {style.STR}.all{RESET} to include all information
  {style.STR}.ret{RESET} to return the inspected {style.CODE}object{RESET}
  {style.STR}.str{RESET} to return the output string instead of printing
  {style.STR}.gray{RESET} to disable colorful output in the console
  {style.STR}.color{RESET} to enforce colorful outputs in the console
Call {style.CODE}wat.locals{RESET} or {style.CODE}wat(){RESET} to inspect local variables.
Call {style.CODE}wat.globals{RESET} to inspect global variables.'''
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
        long = self._inspect_kwargs.get('long', False)
        lines = list(_render_variables(variables, title, long))
        return self._display_output('\n'.join(lines))

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
        elif name in {'long', 'dunder', 'code', 'nodocs', 'caller', 'public', 'all'}:
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


class Style:
    BAR = '\033[0;34m'  # blue
    TRAIT = '\033[1;34m'  # bright blue
    HEAD = '\033[1;37m'  # bright white
    STR = '\033[0;32m'  # green
    NUMBER = '\033[0;31m'  # red
    NONE = '\033[0;35m'  # magenta
    TRUE = '\033[1;32m'  # bright green
    FALSE = '\033[1;31m'  # bright red
    DOCS = '\033[2;37m'  # gray
    KEYWORD = '\033[0;34m'  # blue
    CALLABLE = '\033[1;32m'  # bright green
    SIGNATURE = '\033[0;32m'  # green
    VARIABLE = '\033[1;33m'  # bright yellow
    CODE = '\033[0;33m'  # yellow

    def __init__(self):
        for chunk in filter(bool, os.environ.get('WAT_COLORS', '').split(',')):
            name, code = chunk.strip().split('=')
            setattr(self, name.upper(), f'\033[{code}m')


RESET = '\033[0m'
style = Style()
wat = Wat()
