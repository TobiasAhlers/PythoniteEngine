from typing import Literal, Any

from ..types.base import TypeRepresentation
from ..scope import Scope

from .base import VariableRepresentation


class VariableInitialization(VariableRepresentation):
    """
    Represents a variable initialization in the Pythonite engine.

    Attributes:
        variable_name (str): The name of the variable declared.
        type (TypeRepresentation): The type of the variable declared.
        value (Any): The value to initialize the variable with.
        scope (Literal["global", "local"]): The scope of the variable declared.
    """

    type: TypeRepresentation
    value: Any
    scope: Literal["global", "local"]

    def execute(self, scope: Scope, *args, **kwargs) -> None:
        """
        Execute the variable initialization represented by this class.

        Raises:
            VariableAlreadyDeclaredError: If the variable represented by this class is already declared.

        >>> from pythonite_engine.variable import VariableInitialization
        >>> from pythonite_engine.types import TypeRepresentation
        >>> variable_name = "my_var"
        >>> type = TypeRepresentation()
        >>> value = 5
        >>> scope = "local"
        >>> variable = VariableInitialization(variable_name, type, value, scope)
        >>> variable.execute()
        """
        scope.declare_variable(self)
        scope.set_variable_value(self.variable_name, self.value)
