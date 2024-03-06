from typing import Literal, Any, ClassVar

from ..types.base import TypeRepresentation
from ..utils import execute_representations
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

    __pythonite_signature__: ClassVar[str] = "VariableInitialization"

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
        variable_name = execute_representations(self.variable_name, scope=scope, *args, **kwargs)
        variable_scope = execute_representations(self.scope, scope=scope, *args, **kwargs)
        value = execute_representations(self.value, scope=scope, *args, **kwargs)

        scope.declare_variable(
            variable_name=variable_name, type=self.type, scope=variable_scope
        )
        scope.set_variable_value(variable_name=variable_name, value=value)
