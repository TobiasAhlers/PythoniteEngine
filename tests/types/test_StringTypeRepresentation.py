import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert StringTypeRepresentation.__pythonite_signature__ == "StringType"


def test_convert_value():
    string_type = StringTypeRepresentation()
    assert string_type.convert_value("Hello") == "Hello"
    assert string_type.convert_value(1) == "1"
    assert string_type.convert_value(True) == "True"
    assert string_type.convert_value(1.5) == "1.5"
    assert string_type.convert_value([1, 2, 3]) == "[1, 2, 3]"
    assert string_type.convert_value({"a": 1, "b": 2}) == "{'a': 1, 'b': 2}"


def test_get_type():
    assert StringTypeRepresentation().get_type() == str


def test_execute():
    string_type = StringTypeRepresentation()
    assert string_type.execute("Hello", Scope()) == "Hello"
    assert string_type.execute(1, Scope()) == "1"
    assert string_type.execute(True, Scope()) == "True"
    assert string_type.execute(1.5, Scope()) == "1.5"
    assert string_type.execute([1, 2, 3], Scope()) == "[1, 2, 3]"
    assert string_type.execute({"a": 1, "b": 2}, Scope()) == "{'a': 1, 'b': 2}"
