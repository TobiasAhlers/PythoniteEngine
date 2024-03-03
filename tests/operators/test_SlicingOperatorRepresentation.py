import pytest


from pythonite_engine import *


def test_execute():
    assert SlicingOperatorRepresentation(
        start=0, stop=3, step=1, operands=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ).execute() == [0, 1, 2]

    assert SlicingOperatorRepresentation(
        stop=3, step=1, operands=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ).execute() == [0, 1, 2]

    assert SlicingOperatorRepresentation(
        step=1, operands=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ).execute() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert SlicingOperatorRepresentation(
        step=2, operands=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ).execute() == [0, 2, 4, 6, 8]
