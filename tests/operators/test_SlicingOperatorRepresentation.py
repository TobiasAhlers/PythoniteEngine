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


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x1", type=IntegerTypeRepresentation())
    scope.set_variable_value("x1", 0)

    assert SlicingOperatorRepresentation(
        stop=3,
        step=1,
        operands=[0, 1, VariableRetrieval(variable_name="x1"), 3, 4, 5, 6, 7, 8, 9],
    ).execute(scope=scope, engine=engine) == [0, 1, 0]
