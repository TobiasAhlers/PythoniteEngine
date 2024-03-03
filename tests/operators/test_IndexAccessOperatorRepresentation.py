import pytest


from pythonite_engine import *


def test_execute():
    index_access = IndexAccessOperatorRepresentation(
        index="key", operands={"key": "value"}
    )
    assert index_access.execute() == "value"

    index_access = IndexAccessOperatorRepresentation(index=1, operands=[0, 1])
    assert index_access.execute() == 1
