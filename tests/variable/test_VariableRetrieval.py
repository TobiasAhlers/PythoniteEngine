import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert VariableRetrieval.__pythonite_signature__ == "VariableRetrieval"


def test_execute():
    scope = Scope()
    scope.declare_variable(
        variable_name="my_var", type=IntegerTypeRepresentation(), scope="local"
    )
    scope.set_variable_value(variable_name="my_var", value=5)

    variable = VariableRetrieval(variable_name="my_var")

    assert variable.execute(scope=scope) == 5

    with pytest.raises(VariableNotFoundError):
        VariableRetrieval(variable_name="my_var_not_found").execute(scope=scope)
