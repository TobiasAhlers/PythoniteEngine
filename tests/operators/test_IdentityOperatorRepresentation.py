import pytest


from pythonite_engine import *


def test_execute():
    identity = IdentityOperatorRepresentation(operator="is", operands=[1, 2])
    assert identity.execute() == False

    identity = IdentityOperatorRepresentation(operator="is not", operands=[1, 2])
    assert identity.execute() == True


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    identity = IdentityOperatorRepresentation(
        operator="is", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert identity.execute(scope=scope, engine=engine) == True

    identity = IdentityOperatorRepresentation(
        operator="is not", operands=[VariableRetrieval(variable_name="x"), 10]
    )
    assert identity.execute(scope=scope, engine=engine) == False
