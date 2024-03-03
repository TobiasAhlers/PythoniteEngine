import pytest

from pythonite_engine import *


def test_local_no_parent():
    scope = Scope()
    scope.variables = {"my_var": {"type": IntegerTypeRepresentation(), "value": 10}}

    assert scope.get_variable_value("my_var") == 10


def test_local_with_parent():
    parent_scope = Scope()
    parent_scope.variables = {
        "my_var": {"type": IntegerTypeRepresentation(), "value": 5}
    }

    scope = Scope(parent=parent_scope)
    scope.variables = {"my_var": {"type": IntegerTypeRepresentation(), "value": 10}}

    assert scope.get_variable_value("my_var") == 10


def test_global_with_parent():
    parent_scope = Scope()
    parent_scope.variables = {
        "my_var": {"type": IntegerTypeRepresentation(), "value": 5}
    }

    scope = Scope(parent=parent_scope)

    assert scope.get_variable_value("my_var") == 5


def test_variable_not_existing():
    scope = Scope()
    with pytest.raises(VariableNotFoundError):
        scope.get_variable_value("my_var")


def test_variable_not_existing_with_parent():
    parent_scope = Scope()
    scope = Scope(parent=parent_scope)
    with pytest.raises(VariableNotFoundError):
        scope.get_variable_value("my_var")


def test_variable_declared_but_not_initialized():
    scope = Scope()
    scope.variables = {"my_var": {"type": IntegerTypeRepresentation()}}

    with pytest.raises(VariableDeclaredButNotInitializedError):
        scope.get_variable_value("my_var")
