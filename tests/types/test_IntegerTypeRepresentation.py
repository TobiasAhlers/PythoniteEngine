import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert IntegerTypeRepresentation.__pythonite_signature__ == "IntegerType"


def test_convert_value():
    integer_type = IntegerTypeRepresentation()
    assert integer_type.convert_value(1) == 1
    assert integer_type.convert_value(1.5) == 1
    assert integer_type.convert_value("1") == 1

    with pytest.raises(ConversionError) as e:
        integer_type.convert_value("Hello")


def test_get_type():
    assert IntegerTypeRepresentation().get_type() == int


def test_execute():
    integer_type = IntegerTypeRepresentation()
    assert integer_type.execute(1, Scope()) == 1
    assert integer_type.execute(1.5, Scope()) == 1
    assert integer_type.execute("1", Scope()) == 1

    with pytest.raises(ConversionError) as e:
        integer_type.execute("Hello", Scope())
