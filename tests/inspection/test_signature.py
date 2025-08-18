import inspect
from typing import List, Optional, Any

from tests.asserts import strip_ansi_colors
from wat.inspection.inspection import _get_callable_signature


def _assert_signature_str_equals(obj):
    signature = _get_callable_signature(obj.__name__, obj)
    prefix = strip_ansi_colors(signature).split('(')[0]
    assert strip_ansi_colors(signature) == f'{prefix}{str(inspect.signature(obj))}'


def test_signature_simple():
    def foo(a, b: int, c: str = 'bar', d: bool = True, e: Optional[List[int]] = None) -> str:
        return ''
    _assert_signature_str_equals(foo)


def test_signature_str():
    _assert_signature_str_equals(''.rjust)
    _assert_signature_str_equals(''.replace)
    _assert_signature_str_equals(''.encode)


def test_signature_positional_only():
    def foo(a, b, /, c, d):
        pass
    _assert_signature_str_equals(foo)


def test_signature_keyword_only():
    def foo(a, b, *, c, d):
        pass
    _assert_signature_str_equals(foo)


def test_signature_positional_and_keyword_only():
    def foo(a, /, b, *, c):
        pass
    _assert_signature_str_equals(foo)


def test_signature_varkw():
    def foo(**kwargs):
        pass
    _assert_signature_str_equals(foo)


def test_signature_vararg():
    def foo(*args):
        pass
    _assert_signature_str_equals(foo)


def test_signature_vararg_and_kw():
    def foo(a, *args, b: int, **kwargs):
        pass
    _assert_signature_str_equals(foo)


def test_signature_class():
    class Foo:
        def __init__(self, a: int, b: str = 'bar'):
            pass
    signature = _get_callable_signature(Foo.__name__, Foo)
    prefix = strip_ansi_colors(signature).split('(')[0]
    assert strip_ansi_colors(signature) == f"{prefix}{str(inspect.signature(Foo))}"


def test_signature_typing_any():
    def foo(a: Any):
        pass
    _assert_signature_str_equals(foo)


def test_signature_colors():
    def foo(a_a: int, b_b: str = 'bar') -> str:
        return ''
    BLUE = '\033[0;34m'
    BRIGHT_GREEN = '\033[1;32m'
    GREEN = '\033[0;32m'
    RESET = '\033[0m'
    YELLOW = '\033[0;33m'
    signature = _get_callable_signature(foo.__name__, foo)
    assert signature.startswith(f'{BLUE}def {BRIGHT_GREEN}foo{GREEN}({RESET}')
    assert f'a_a{RESET}{GREEN}: {RESET}{YELLOW}int{RESET}' in signature
    assert f"b_b{RESET}{GREEN}: {RESET}{YELLOW}str{RESET}{GREEN} = {RESET}{GREEN}'bar'{RESET}" in signature
    assert f'{GREEN}){RESET}{GREEN} -> {RESET}{YELLOW}str{RESET}' in signature
