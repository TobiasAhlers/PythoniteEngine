import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert StaticValue.__pythonite_signature__ == "StaticValue"


def test_execute():
    static_value = StaticValue(type=IntegerTypeRepresentation(), value=5)

    assert static_value.execute(scope=Scope()) == 5

    static_value = StaticValue(type=StringTypeRepresentation(), value=12)

    assert static_value.execute(scope=Scope()) == "12"
