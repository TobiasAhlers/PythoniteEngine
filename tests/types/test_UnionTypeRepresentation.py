import pytest

from typing import Union

from pythonite_engine import *


def test_pythonite_signature():
    assert UnionTypeRepresentation.__pythonite_signature__ == "UnionType"


def test_convert_value():
    assert (
        UnionTypeRepresentation(
            types=[IntegerTypeRepresentation(), StringTypeRepresentation()]
        ).convert_value(1)
        == 1
    )
    assert (
        UnionTypeRepresentation(
            types=[IntegerTypeRepresentation(), StringTypeRepresentation()]
        ).convert_value("Hello")
        == "Hello"
    )

    with pytest.raises(ConversionError) as e:
        UnionTypeRepresentation(types=[IntegerTypeRepresentation()]).convert_value(
            "INVALID"
        )


def test_get_type():
    assert (
        UnionTypeRepresentation(
            types=[IntegerTypeRepresentation(), StringTypeRepresentation()]
        ).get_type()
        == Union[str, int]
    )


def test_execute():
    union_type = UnionTypeRepresentation(
        types=[IntegerTypeRepresentation(), StringTypeRepresentation()]
    )
    assert union_type.execute(1, Scope()) == 1
    assert union_type.execute("Hello", Scope()) == "Hello"

    with pytest.raises(ConversionError) as e:
        UnionTypeRepresentation(types=[IntegerTypeRepresentation()]).execute(
            "INVALID", Scope()
        )
