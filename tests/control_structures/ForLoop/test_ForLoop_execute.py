import pytest

from pythonite_engine import *


def test_execute_all_direct_values():
    assert (
        ForLoop(
            loop_variable_name="i",
            iterable=[1, 2, 3],
            loop_varible_annotation=Annotation(type=IntegerTypeRepresentation()),
            body=[StaticValue(value="Hello, World!", type=StringTypeRepresentation())],
        ).execute(Scope())
        == "Hello, World!Hello, World!Hello, World!"
    )


def test_execute_pythonite_representation_as_loop_variable_name():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 0)

    assert (
        ForLoop(
            loop_variable_name=VariableRetrieval(variable_name="x"),
            iterable=[1, 2, 3],
            loop_varible_annotation=Annotation(type=IntegerTypeRepresentation()),
            body=[StaticValue(value="Hello, World!", type=StringTypeRepresentation())],
        ).execute(scope=scope, engine=engine)
        == "Hello, World!Hello, World!Hello, World!"
    )


def test_execute_pythonite_representation_as_iterable():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(
        variable_name="x",
        type=ListTypeRepresentation(allowed_types=[IntegerTypeRepresentation()]),
    )
    scope.set_variable_value(variable_name="x", value=[1, 2, 3])
    print(scope.variables)
    assert (
        ForLoop(
            loop_variable_name="i",
            iterable=VariableRetrieval(variable_name="x"),
            loop_varible_annotation=Annotation(type=IntegerTypeRepresentation()),
            body=[StaticValue(value="Hello, World!", type=StringTypeRepresentation())],
        ).execute(scope=scope, engine=engine)
        == "Hello, World!Hello, World!Hello, World!"
    )


def test_execute_pythonite_representation_as_body():
    engine = PythoniteEngine()
    scope = Scope()
    scope.declare_variable(variable_name="x", type=IntegerTypeRepresentation())
    scope.set_variable_value("x", 0)

    assert (
        ForLoop(
            loop_variable_name="i",
            iterable=[1, 2, 3],
            loop_varible_annotation=Annotation(type=IntegerTypeRepresentation()),
            body=[VariableRetrieval(variable_name="x")],
        ).execute(scope=scope, engine=engine)
        == "0" * 3
    )
