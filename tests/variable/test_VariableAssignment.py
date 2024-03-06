import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert VariableAssignment.__pythonite_signature__ == "VariableAssignment"


def test_execute():
    parent_scope = Scope()
    scope = Scope(parent=parent_scope)

    variable_declaration = VariableDeclaration(
        variable_name="my_var",
        type=IntegerTypeRepresentation(),
        scope="local",
    )
    variable_declaration.execute(scope=scope)

    variable_assignment = VariableAssignment(
        variable_name="my_var",
        value=5,
    )
    variable_assignment.execute(scope=scope)

    assert scope.variables == {
        "my_var": {"type": IntegerTypeRepresentation(), "value": 5}
    }

    with pytest.raises(VariableNotFoundError):
        VariableAssignment(
            variable_name="my_var_not_found",
            value=5,
        ).execute(scope=scope)

    variable_declaration = VariableDeclaration(
        variable_name="global_var",
        type=IntegerTypeRepresentation(),
        scope="global",
    )
    variable_declaration.execute(scope=scope)

    variable_assignment = VariableAssignment(
        variable_name="global_var",
        value=5,
    )
    variable_assignment.execute(scope=scope)

    assert parent_scope.variables == {
        "global_var": {"type": IntegerTypeRepresentation(), "value": 5}
    }
    assert scope.variables == {
        "my_var": {"type": IntegerTypeRepresentation(), "value": 5}
    }
