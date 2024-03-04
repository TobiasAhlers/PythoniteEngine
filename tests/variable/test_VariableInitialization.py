import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert VariableInitialization.__pythonite_signature__ == "VariableInitialization"


def test_execute():
    scope = Scope()
    variable = VariableInitialization(
        variable_name="my_var",
        type=IntegerTypeRepresentation(),
        value=5,
        scope="local",
    )

    variable.execute(scope=scope)

    assert scope.variables == {
        "my_var": {
            "type": IntegerTypeRepresentation(),
            "value": 5,
        }
    }

    with pytest.raises(VariableAlreadyDeclaredError):
        VariableInitialization(
            variable_name="my_var",
            type=IntegerTypeRepresentation(),
            value=5,
            scope="local",
        ).execute(scope=scope)
