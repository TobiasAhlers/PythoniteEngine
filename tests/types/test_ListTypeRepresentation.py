import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert ListTypeRepresentation.__pythonite_signature__ == "ListType"


def test_convert_value():
    list_type = ListTypeRepresentation()
    assert list_type.convert_value([1, 2, 3]) == [1, 2, 3]
    assert list_type.convert_value([1, "Hello", 3]) == [1, "Hello", 3]
    assert list_type.convert_value([]) == []
    assert list_type.convert_value([1]) == [1]
    assert list_type.convert_value(["Hello"]) == ["Hello"]
    assert list_type.convert_value([True]) == [True]
    assert list_type.convert_value([1.5]) == [1.5]
    assert list_type.convert_value([{"a": 1, "b": 2}]) == [{"a": 1, "b": 2}]

    with pytest.raises(ConversionError) as e:
        list_type.convert_value(1)

    list_type = ListTypeRepresentation(allowed_types=[IntegerTypeRepresentation()])
    assert list_type.convert_value([1, 2, 3]) == [1, 2, 3]
    assert list_type.convert_value(["1"]) == [1]

    with pytest.raises(ConversionError) as e:
        list_type.convert_value(["Hello"])


def test_get_type():
    assert ListTypeRepresentation().get_type() == list


def test_execute():
    list_type = ListTypeRepresentation()
    assert list_type.execute([1, 2, 3], Scope()) == [1, 2, 3]
    assert list_type.execute([1, "Hello", 3], Scope()) == [1, "Hello", 3]
    assert list_type.execute([], Scope()) == []
    assert list_type.execute([1], Scope()) == [1]
    assert list_type.execute(["Hello"], Scope()) == ["Hello"]
    assert list_type.execute([True], Scope()) == [True]
    assert list_type.execute([1.5], Scope()) == [1.5]
    assert list_type.execute([{"a": 1, "b": 2}], Scope()) == [{"a": 1, "b": 2}]

    with pytest.raises(ConversionError) as e:
        list_type.execute(1, Scope())
