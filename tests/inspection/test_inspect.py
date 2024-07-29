from datetime import datetime
from enum import Enum
import os
import re

from pydantic import BaseModel

import wat
from wat.inspection.inspection import inspect_format
from tests.asserts import assert_multiline_match, strip_ansi_colors, StdoutCap


def test_inspect_primitive_var():
    output = inspect_format(None)
    assert strip_ansi_colors(output) == """
value: None
type: NoneType
""".strip()

    output = inspect_format([5])
    assert strip_ansi_colors(output) == """
value: [
    5,
]
type: list
len: 1

Public attributes:
  def append(object, /) # Append object to the end of the list.
  def clear() # Remove all items from list.
  def copy() # Return a shallow copy of the list.
  def count(value, /) # Return number of occurrences of value.
  def extend(iterable, /) # Extend list by appending elements from the iterable.
  def index(value, start=0, stop=9223372036854775807, /) # Return first index of value.…
  def insert(index, object, /) # Insert object before index.
  def pop(index=-1, /) # Remove and return item at index (default last).…
  def remove(value, /) # Remove first occurrence of value.…
  def reverse() # Reverse *IN PLACE*.
  def sort(*, key=None, reverse=False) # Sort the list in ascending order and return None.…
""".strip()
    
    output = inspect_format([5], dunder=True)
    assert "def __eq__(value, /) # Return self==value." in strip_ansi_colors(output)

    output = inspect_format('poo', short=True)
    assert_multiline_match(output, r'''
value: 'poo'
type: str
len: 3
''')


def test_inspect_instance():
    class Hero:
        """
        A hero
        """
        def __init__(self, name: str):
            self.a = name
        
        def shout(self, loudness: int) -> str:
            """Do something very very very very very very very very very very very very very very very very very stupid"""
            return self.a * loudness
    
    instance = Hero('batman')
    output = inspect_format(instance)
    assert_multiline_match(output, r'''
value: <test_inspect\.test_inspect_instance\.<locals>\.Hero object at .*>
type: test_inspect\.Hero

Public attributes:
  a: str = 'batman'

  def shout\(loudness: int\) -> str \# Do something very very very very very very very very very very very very very very very very very st…
''')
                           
    output = inspect_format(Hero)
    assert_multiline_match(output, r'''
value: <class 'test_inspect\.test_inspect_instance\.<locals>\.Hero'>
type: type
signature: class Hero\(name: str\)
"""A hero"""

Public attributes:
  def shout\(self, loudness: int\) -> str \# Do something very very very very very very very very very very very very very very very very very st…
''')


def test_inspect_function():
    def foo(a: int, b: str = 'bar') -> str:
        """
        Do something
        dumb
        """
        return a * b
  
    output = inspect_format(foo)
    print(output)
    assert_multiline_match(output, r'''
value: <function test_inspect_function\.<locals>\.foo at .*>
type: function
signature: def foo\(a: int, b: str = 'bar'\) -> str
"""
Do something
dumb
"""
''')


def test_inspect_nested_dict():
    output = inspect_format({
        'a': {
            'b': {
                'values': [2,5,3],
            },
            "empty_dict": {},
            "empty_list": [],
            40: None,
            None: 42,
        },
    }, short=True)
    assert_multiline_match(output, r'''
value: {
    'a': {
        'b': {
            'values': \[
                2,
                5,
                3,
            \],
        },
        'empty_dict': {},
        'empty_list': \[\],
        40: None,
        None: 42,
    },
}
type: dict
len: 1
''')


def test_inspect_datetime_repr():
    output = inspect_format(datetime(2023, 8, 1), short=True)
    assert_multiline_match(output, r'''
str: 2023-08-01 00:00:00
repr: datetime.datetime\(2023, 8, 1, 0, 0\)
type: datetime.datetime
parents: datetime\.date
''')


def test_inspect_long():
    output = inspect_format(datetime, long=True, code=True)
    lines = output.splitlines()
    assert "value: <class 'datetime.datetime'>" in lines
    assert "type: type" in lines
    assert "signature: class datetime(…)" in lines
    assert "datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])" in lines


def test_inspect_source_code():
    class Sorcerer:
        def __init__(self):
            self.level = 1
        def level_up(self):
            self.level += 1

    output = inspect_format(Sorcerer, code=True)
    lines = output.splitlines()
    assert "value: <class 'test_inspect.test_inspect_source_code.<locals>.Sorcerer'>" in lines
    assert "type: type" in lines
    assert "signature: class Sorcerer()" in lines
    assert "source code:" in lines
    assert "    class Sorcerer:" in lines
    assert "            self.level += 1" in lines


def test_inspect_async_def():
    async def looper():
        pass
    output = inspect_format(looper, short=True)
    assert_multiline_match(output, r'''
value: <function test_inspect_async_def.<locals>.looper at .*>
type: function
signature: async def looper\(\)
''')


def test_wat_with_nothing():
    assert str(wat) == '<Wat Inspector object>'
    with StdoutCap() as capture:
        assert repr(wat) == ''
    assert 'Try wat / object or wat.modifiers / object to inspect an object. Modifiers are:' in capture.uncolor().splitlines()


def test_wat_locals():
    _local_var = 23
    with StdoutCap() as capture:
        wat()
    assert 'value: <wat.inspection.inspection.locals object' in capture.uncolor()
    assert '_local_var: int = 23' in capture.uncolor()

    with StdoutCap() as capture:
        wat.locals
    assert 'value: <wat.inspection.inspection.locals object' in capture.uncolor()
    assert '_local_var: int = 23' in capture.uncolor()


global_var = 23

def test_wat_globals():
    with StdoutCap() as capture:
        wat.globals
    assert 'value: <wat.inspection.inspection.globals object' in capture.uncolor()
    assert 'global_var: int = 23' in capture.uncolor()


def test_wat_with_object():
    with StdoutCap() as capture:
        wat(short=True) / 'moo'
    assert_multiline_match(capture.output(), r'''
value: 'moo'
type: str
len: 3
''')

    with StdoutCap() as capture:
        wat('moo', short=True)
    assert_multiline_match(capture.output(), r'''
value: 'moo'
type: str
len: 3
''')


def test_wat_with_short_long_modifiers():
    with StdoutCap() as capture:
        wat.short('moo')
    assert_multiline_match(capture.output(), r'''
value: 'moo'
type: str
len: 3
''')

    with StdoutCap() as capture:
        wat.long / 'moo2'
    assert r'''
  def capitalize():
"""
''' in capture.output()


def test_wat_with_multiple_modifiers():
    with StdoutCap() as capture:
        wat.dunder.code / re.match

    assert '''
Dunder attributes:
''' in capture.output()
    assert '''  def __eq__(value, /)''' in capture.output()
    
    assert '''
source code:
def match(pattern, string, flags=0):
''' in capture.output()
    

def test_wat_modifiers_all_but_nodocs():
    with StdoutCap() as capture:
        wat.all.short.nodocs / re.match
    assert_multiline_match(capture.output(), r'''
value: <function match at .*>
type: function
signature: def match\(pattern, string, flags=0\)
source code:
def match\(pattern, string, flags=0\):
    """.*
    .*"""
    .*
''')


def test_list_parent_classes():
    class Parent(str, Enum):
        FIRST = 'first'

    output = inspect_format(Parent.FIRST, short=True)
    assert_multiline_match(output, r'''
str: '(Parent\.FIRST|first)'
repr: <Parent\.FIRST: 'first'>
type: test_inspect\.Parent
parents: str, enum\.Enum
len: 5
''')
    

def test_list_deep_mro_classes():
    class Grand(object):
        pass

    class Father(Grand):
        pass

    class Son(Father):
        pass

    output = inspect_format(Son(), short=True)
    assert_multiline_match(output, r'''
value: <test_inspect.test_list_deep_mro_classes.<locals>.Son object at .*>
type: test_inspect.Son
parents: test_inspect.Father, test_inspect.Grand
''')


def test_pydantic_class():
    class Person(BaseModel):
        name: str

    output = inspect_format(Person(name='george'), short=True)
    assert_multiline_match(output, r'''
str: name='george'
repr: Person\(name='george'\)
type: test_inspect\.Person
parents: pydantic\.main\.BaseModel
''')


def test_returning_inspected_object():
    assert wat.short.ret / 'hello' == 'hello'


def test_listing_private_attributes():
    class Foo:
        def __init__(self, name: str):
            self._name = name
        
        def _private_method(self):
            pass
    
    output = inspect_format(Foo('bar'))
    assert_multiline_match(output, r'''
value: <test_inspect\.test_listing_private_attributes\.<locals>\.Foo object at .*>
type: test_inspect\.Foo

Private attributes:
  _name: str = 'bar'

  def _private_method\(\)
''')


def test_backwards_wat_wat_import():
    from wat import wat
    assert wat.ret / 'foo' == 'foo'


def test_wat_return_output():
    result = wat.short.str / 'foo'
    assert_multiline_match(result, r'''
value: 'foo'
type: str
len: 3
''')


def test_colorful_output():
    try:
        os.environ['WAT_COLOR'] = 'false'
        output = inspect_format(None)
        assert output == """value: None
type: NoneType"""

        os.environ['WAT_COLOR'] = 'true'
        output = inspect_format(None)
        assert output == """\x1b[1;34mvalue:\x1b[0m \x1b[0;35mNone\x1b[0m
\x1b[1;34mtype:\x1b[0m \x1b[0;33mNoneType\x1b[0m"""
    finally:
        os.environ['WAT_COLOR'] = ''
