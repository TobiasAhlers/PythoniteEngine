import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert VariableDeclaration.__pythonite_signature__ == "VariableDeclaration"


def test_execute():
    parent_scope = Scope()
    scope = Scope(parent=parent_scope)

    variable_declaration = VariableDeclaration(
        variable_name="my_var",
        type=IntegerTypeRepresentation(),
        scope="local",
    )
    variable_declaration.execute(scope=scope)

    assert scope.variables == {"my_var": {"type": IntegerTypeRepresentation()}}

    with pytest.raises(VariableAlreadyDeclaredError):
        VariableDeclaration(
            variable_name="my_var",
            type=IntegerTypeRepresentation(),
            scope="local",
        ).execute(scope=scope)

    variable_declaration = VariableDeclaration(
        variable_name="global_var",
        type=IntegerTypeRepresentation(),
        scope="global",
    )
    variable_declaration.execute(scope=scope)

    assert parent_scope.variables == {
        "global_var": {"type": IntegerTypeRepresentation()}
    }
    assert scope.variables == {"my_var": {"type": IntegerTypeRepresentation()}}
