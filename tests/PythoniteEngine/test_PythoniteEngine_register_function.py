import pytest

from pythonite_engine import *


def test_register_unregistered_function():
    engine = PythoniteEngine()

    def my_function(x):
        return x + 1

    engine.register_function("my_function", my_function)
    assert engine.functions["my_function"] == my_function


def test_register_registered_function():
    engine = PythoniteEngine()

    def my_function(x):
        return x + 1

    engine.register_function("my_function", my_function)
    with pytest.raises(FunctionAlreadyRegisteredError):
        engine.register_function("my_function", my_function)
