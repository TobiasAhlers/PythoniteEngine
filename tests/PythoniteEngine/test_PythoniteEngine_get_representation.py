import pytest

from pythonite_engine import *


def test_get_registered_representation():
    engine = PythoniteEngine()

    class MyRepresentation(PythoniteRepresentation):
        __pythonite_signature__ = "MyRepresentation"

    engine.representations["MyRepresentation"] = MyRepresentation
    assert engine.get_representation("MyRepresentation") == MyRepresentation


def test_get_unregistered_representation():
    engine = PythoniteEngine()

    with pytest.raises(RepresentationNotFoundError):
        engine.get_representation("MyRepresentation")
