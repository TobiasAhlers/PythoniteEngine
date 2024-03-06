import pytest


from pythonite_engine import *


def test_execute():
    index_access = IndexAccessOperatorRepresentation(
        index="key", operands={"key": "value"}
    )
    assert index_access.execute() == "value"

    index_access = IndexAccessOperatorRepresentation(index=1, operands=[0, 1])
    assert index_access.execute() == 1


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 0)

    index_access = IndexAccessOperatorRepresentation(
        index=0,
        operands=[0, 1, VariableRetrieval(variable_name="x"), 3, 4, 5, 6, 7, 8, 9],
    )
    assert index_access.execute(scope=scope, engine=engine) == 0
