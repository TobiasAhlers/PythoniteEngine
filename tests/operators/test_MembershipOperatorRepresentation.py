import pytest


from pythonite_engine import *


def test_execute():
    membership = MembershipOperatorRepresentation(operator="in", operands=[1, [1, 2]])
    assert membership.execute() == True

    membership = MembershipOperatorRepresentation(
        operator="not in", operands=[1, [1, 2]]
    )
    assert membership.execute() == False


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    membership = MembershipOperatorRepresentation(
        operator="in", operands=[VariableRetrieval(variable_name="x"), [10, 20]]
    )
    assert membership.execute(scope=scope, engine=engine) == True

    membership = MembershipOperatorRepresentation(
        operator="not in", operands=[VariableRetrieval(variable_name="x"), [10, 20]]
    )
    assert membership.execute(scope=scope, engine=engine) == False
