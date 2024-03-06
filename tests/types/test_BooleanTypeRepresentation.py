import pytest

from typing import Any

from pythonite_engine import *


def test_pythonite_signature():
    assert BooleanTypeRepresentation.__pythonite_signature__ == "BooleanType"


def test_convert_value():
    boolean_type = BooleanTypeRepresentation()
    assert boolean_type.convert_value(True) == True
    assert boolean_type.convert_value(False) == False
    assert boolean_type.convert_value(1) == True
    assert boolean_type.convert_value(0) == False
    assert boolean_type.convert_value("True") == True
    assert boolean_type.convert_value("False") == True
    assert boolean_type.convert_value("true") == True
    assert boolean_type.convert_value("false") == True


def test_get_type():
    assert BooleanTypeRepresentation().get_type() == bool


def test_execute():
    boolean_type = BooleanTypeRepresentation()
    assert boolean_type.execute(True, Scope()) == True
    assert boolean_type.execute(False, Scope()) == False
    assert boolean_type.execute(1, Scope()) == True
    assert boolean_type.execute(0, Scope()) == False
    assert boolean_type.execute("True", Scope()) == True
    assert boolean_type.execute("False", Scope()) == True
