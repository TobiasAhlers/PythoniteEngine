import pytest

from pythonite_engine import *


def test_signature():
    assert Annotation.__pythonite_signature__ == "Annotation"
