import pytest

from datetime import date

from pythonite_engine import *


def test_pythonite_signature():
    assert DictionaryTypeRepresentation.__pythonite_signature__ == "DictionaryType"


def test_convert_value():
    dictionary_type = DictionaryTypeRepresentation()
    assert dictionary_type.convert_value({"a": 1, "b": 2}) == {"a": 1, "b": 2}
    assert dictionary_type.convert_value({1: "a", 2: "b"}) == {1: "a", 2: "b"}
    assert dictionary_type.convert_value({1: 1, 2: 2}) == {1: 1, 2: 2}
    assert dictionary_type.convert_value({1: 1, "2": "2"}) == {1: 1, "2": "2"}
    assert dictionary_type.convert_value({1: 1, "2": "2"}) == {1: 1, "2": "2"}
    assert dictionary_type.convert_value({1: 1, "2": "2"}) == {1: 1, "2": "2"}

    with pytest.raises(ConversionError) as e:
        dictionary_type.convert_value(1)


def test_get_type():
    assert DictionaryTypeRepresentation().get_type() == dict


def test_execute():
    dictionary_type = DictionaryTypeRepresentation()
    assert dictionary_type.execute({"a": 1, "b": 2}, Scope()) == {"a": 1, "b": 2}
    assert dictionary_type.execute({1: "a", 2: "b"}, Scope()) == {1: "a", 2: "b"}
    assert dictionary_type.execute({1: 1, 2: 2}, Scope()) == {1: 1, 2: 2}
    assert dictionary_type.execute({1: 1, "2": "2"}, Scope()) == {1: 1, "2": "2"}
    assert dictionary_type.execute({1: 1, "2": "2"}, Scope()) == {1: 1, "2": "2"}
    assert dictionary_type.execute({1: 1, "2": "2"}, Scope()) == {1: 1, "2": "2"}
   
    with pytest.raises(ConversionError) as e:
        dictionary_type.execute(1, Scope())