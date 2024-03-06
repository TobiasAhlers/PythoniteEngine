import pytest


from pythonite_engine import *


def test_execute():
    arithmetic = ArithmeticOperatorRepresentation(operator="+", operands=[1, 2])
    assert arithmetic.execute() == 3

    arithmetic = ArithmeticOperatorRepresentation(operator="-", operands=[1, 2])
    assert arithmetic.execute() == -1

    arithmetic = ArithmeticOperatorRepresentation(operator="*", operands=[1, 2])
    assert arithmetic.execute() == 2

    arithmetic = ArithmeticOperatorRepresentation(operator="/", operands=[1, 2])
    assert arithmetic.execute() == 0.5

    arithmetic = ArithmeticOperatorRepresentation(operator="//", operands=[1, 2])
    assert arithmetic.execute() == 0

    arithmetic = ArithmeticOperatorRepresentation(operator="%", operands=[1, 2])
    assert arithmetic.execute() == 1

    arithmetic = ArithmeticOperatorRepresentation(operator="**", operands=[1, 2])
    assert arithmetic.execute() == 1


def test_execute_with_pythonite_representation():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    arithmetic = ArithmeticOperatorRepresentation(
        operator="+", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 15

    arithmetic = ArithmeticOperatorRepresentation(
        operator="-", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 5

    arithmetic = ArithmeticOperatorRepresentation(
        operator="*", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 50

    arithmetic = ArithmeticOperatorRepresentation(
        operator="/", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 2.0

    arithmetic = ArithmeticOperatorRepresentation(
        operator="//", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 2

    arithmetic = ArithmeticOperatorRepresentation(
        operator="%", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 0

    arithmetic = ArithmeticOperatorRepresentation(
        operator="**", operands=[VariableRetrieval(variable_name="x"), 5]
    )
    assert arithmetic.execute(scope=scope, engine=engine) == 100000
