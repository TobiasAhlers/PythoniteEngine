import pytest

from pythonite_engine import *


def test_execute():
    with pytest.raises(NotImplementedError):
        PythoniteRepresentation().execute(scope=Scope())
