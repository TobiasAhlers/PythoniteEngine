import pytest

from pythonite_engine import *


def test_get_registered_function():
    engine = PythoniteEngine()

    def my_function(x):
        return x + 1

    engine.functions["my_function"] = my_function
    assert engine.get_function("my_function") == my_function


def test_get_unregistered_function():
    engine = PythoniteEngine()

    with pytest.raises(FunctionNotFoundError):
        engine.get_function("my_function")
