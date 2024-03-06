import pytest


from pythonite_engine import *


def test_execute():
    comparison = ComparisonOperatorRepresentation(operator="==", operands=[1, 2])
    assert comparison.execute() == False

    comparison = ComparisonOperatorRepresentation(operator="!=", operands=[1, 2])
    assert comparison.execute() == True

    comparison = ComparisonOperatorRepresentation(operator="<", operands=[1, 2])
    assert comparison.execute() == True

    comparison = ComparisonOperatorRepresentation(operator="<=", operands=[1, 2])
    assert comparison.execute() == True

    comparison = ComparisonOperatorRepresentation(operator=">", operands=[1, 2])
    assert comparison.execute() == False

    comparison = ComparisonOperatorRepresentation(operator=">=", operands=[1, 2])
    assert comparison.execute() == False


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    comparison = ComparisonOperatorRepresentation(
        operator="==", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert comparison.execute(scope=scope, engine=engine) == True

    comparison = ComparisonOperatorRepresentation(
        operator="!=", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert comparison.execute(scope=scope, engine=engine) == False

    comparison = ComparisonOperatorRepresentation(
        operator="<", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert comparison.execute(scope=scope, engine=engine) == False

    comparison = ComparisonOperatorRepresentation(
        operator="<=", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert comparison.execute(scope=scope, engine=engine) == True

    comparison = ComparisonOperatorRepresentation(
        operator=">", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert comparison.execute(scope=scope, engine=engine) == False

    comparison = ComparisonOperatorRepresentation(
        operator=">=", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert comparison.execute(scope=scope, engine=engine) == True
