import pytest

from pythonite_engine import *


def test_execute_consequent():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=StaticValue(
                type=StringTypeRepresentation(), value="x is greater than 5"
            ),
        ).execute(scope=scope, engine=engine)
        == "x is greater than 5"
    )


def test_consequent_any():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=10,
        ).execute(scope=scope, engine=engine)
        == 10
    )


def test_execute_alternate():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 3)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=StaticValue(
                type=StringTypeRepresentation(), value="x is greater than 5"
            ),
            alternate=StaticValue(
                type=StringTypeRepresentation(), value="x is less than 5"
            ),
        ).execute(scope=scope, engine=engine)
        == "x is less than 5"
    )


def test_alternate_none():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 3)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=StaticValue(
                type=StringTypeRepresentation(), value="x is greater than 5"
            ),
        ).execute(scope=scope, engine=engine)
        == None
    )


def test_alternate_any():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 3)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=StaticValue(
                type=StringTypeRepresentation(), value="x is greater than 5"
            ),
            alternate=10,
        ).execute(scope=scope, engine=engine)
        == 10
    )


def test_execute_consequent_list():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 10)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=[
                StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                VariableRetrieval(variable_name="x"),
                StaticValue(value="!", type=StringTypeRepresentation()),
            ],
        ).execute(scope=scope, engine=engine)
        == "Hello, 10!"
    )


def test_alternate_list():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 3)

    assert (
        ConditionalStatement(
            condition=ComparisonOperatorRepresentation(
                operator=">",
                operands=[
                    VariableRetrieval(variable_name="x"),
                    5,
                ],
            ),
            consequent=StaticValue(
                type=StringTypeRepresentation(), value="x is greater than 5"
            ),
            alternate=[
                StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                VariableRetrieval(variable_name="x"),
                StaticValue(value="!", type=StringTypeRepresentation()),
            ],
        ).execute(scope=scope, engine=engine)
        == "Hello, 3!"
    )
