import pytest

from pythonite_engine import *


def test_register_unregistered_representation():
    engine = PythoniteEngine()

    class MyRepresentation(PythoniteRepresentation):
        __pythonite_signature__ = "MyRepresentation"

    engine.register_representation(MyRepresentation)
    assert engine.representations["MyRepresentation"] == MyRepresentation


def test_register_registered_representation():
    engine = PythoniteEngine()

    class MyRepresentation(PythoniteRepresentation):
        __pythonite_signature__ = "MyRepresentation"

    engine.register_representation(MyRepresentation)
    with pytest.raises(RepresentationAlreadyRegisteredError):
        engine.register_representation(MyRepresentation)
