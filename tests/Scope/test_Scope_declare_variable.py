import pytest

from pythonite_engine import *


def test_local_no_parent():
    scope = Scope()
    scope.declare_variable(
        variable_name="my_var", type=IntegerTypeRepresentation(), scope="local"
    )
    assert scope.variables == {"my_var": {"type": IntegerTypeRepresentation()}}


def test_local_with_parent():
    parent_scope = Scope()

    scope = Scope(parent=parent_scope)
    scope.declare_variable(
        variable_name="my_var", type=IntegerTypeRepresentation(), scope="local"
    )
    assert scope.variables == {"my_var": {"type": IntegerTypeRepresentation()}}
    assert parent_scope.variables == {}


def test_global_no_parent():
    scope = Scope()
    scope.declare_variable(
        variable_name="my_var", type=IntegerTypeRepresentation(), scope="global"
    )
    assert scope.variables == {"my_var": {"type": IntegerTypeRepresentation()}}


def test_global_with_parent():
    parent_scope = Scope()

    scope = Scope(parent=parent_scope)
    scope.declare_variable(
        variable_name="my_var", type=IntegerTypeRepresentation(), scope="global"
    )
    assert scope.variables == {}
    assert parent_scope.variables == {"my_var": {"type": IntegerTypeRepresentation()}}


def test_variable_already_declared_error():
    scope = Scope()
    scope.declare_variable(
        variable_name="my_var", type=IntegerTypeRepresentation(), scope="global"
    )
    with pytest.raises(VariableAlreadyDeclaredError):
        scope.declare_variable(
            variable_name="my_var", type=IntegerTypeRepresentation(), scope="global"
        )
