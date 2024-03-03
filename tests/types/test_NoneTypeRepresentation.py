import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert NoneTypeRepresentation.__pythonite_signature__ == "NoneType"


def test_convert_value():
    none_type = NoneTypeRepresentation()
    assert none_type.convert_value(None) == None

    with pytest.raises(ConversionError) as e:
        none_type.convert_value(1)


def test_get_type():
    assert NoneTypeRepresentation().get_type() == type(None)


def test_execute():
    none_type = NoneTypeRepresentation()
    assert none_type.execute(None, Scope()) == None
