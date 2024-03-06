import pytest

from typing import Any

from pythonite_engine import *


def test_pythonite_signature():
    assert AnyTypeRepresentation.__pythonite_signature__ == "AnyType"


def test_convert_value():
    any_type = AnyTypeRepresentation()
    assert any_type.convert_value(1) == 1
    assert any_type.convert_value("Hello") == "Hello"
    assert any_type.convert_value(True) == True
    assert any_type.convert_value(1.5) == 1.5
    assert any_type.convert_value([1, 2, 3]) == [1, 2, 3]
    assert any_type.convert_value({"a": 1, "b": 2}) == {"a": 1, "b": 2}


def test_get_type():
    assert AnyTypeRepresentation().get_type() == Any


def test_execute():
    any_type = AnyTypeRepresentation()
    assert any_type.execute(1, Scope()) == 1
    assert any_type.execute("Hello", Scope()) == "Hello"
    assert any_type.execute(True, Scope()) == True
    assert any_type.execute(1.5, Scope()) == 1.5
    assert any_type.execute([1, 2, 3], Scope()) == [1, 2, 3]
    assert any_type.execute({"a": 1, "b": 2}, Scope()) == {"a": 1, "b": 2}