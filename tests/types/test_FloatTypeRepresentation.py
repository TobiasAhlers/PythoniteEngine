import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert FloatTypeRepresentation.__pythonite_signature__ == "FloatType"


def test_convert_value():
    float_type = FloatTypeRepresentation()
    assert float_type.convert_value(1) == 1.0
    assert float_type.convert_value(1.5) == 1.5
    assert float_type.convert_value("1.5") == 1.5
    assert float_type.convert_value("1") == 1.0

    with pytest.raises(ConversionError) as e:
        float_type.convert_value("Hello")


def test_get_type():
    assert FloatTypeRepresentation().get_type() == float


def test_execute():
    float_type = FloatTypeRepresentation()
    assert float_type.execute(1, Scope()) == 1.0
    assert float_type.execute(1.5, Scope()) == 1.5
    assert float_type.execute("1.5", Scope()) == 1.5
    assert float_type.execute("1", Scope()) == 1.0

    with pytest.raises(ConversionError) as e:
        float_type.execute("Hello", Scope())
