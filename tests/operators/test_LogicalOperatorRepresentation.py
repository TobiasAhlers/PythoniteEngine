import pytest


from pythonite_engine import *


def test_execute():
    logical = LogicalOperatorRepresentation(operator="and", operands=[True, False])
    assert logical.execute() == False

    logical = LogicalOperatorRepresentation(operator="or", operands=[True, False])
    assert logical.execute() == True


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=BooleanTypeRepresentation())
    scope.set_variable_value("x", True)

    logical = LogicalOperatorRepresentation(
        operator="and", operands=[VariableRetrieval(variable_name="x"), False]
    )
    assert logical.execute(scope=scope, engine=engine) == False

    logical = LogicalOperatorRepresentation(
        operator="or", operands=[VariableRetrieval(variable_name="x"), False]
    )
    assert logical.execute(scope=scope, engine=engine) == True
