from typing import Any, ClassVar, Literal

from ..scope import Scope

from .base import VariableRepresentation


class VariableAssignment(VariableRepresentation):
    """
    Represents a variable assignment in the Pythonite engine.

    Attributes:
        variable_name (str): The name of the variable declared.
        type (PythoniteTypeRepresentation): The type of the variable declared.
        scope (Literal["global", "local"]): The scope of the variable declared.
    """

    __pythonite_signature__: ClassVar[str] = "VariableAssignment"

    value: Any
    scope: Literal["global", "local"]

    def execute(self, scope: Scope, *args, **kwargs) -> None:
        """
        Assign the value to the variable represented by this class.

        Args:
            scope (Scope): The scope to use for the assignment.

        Raises:
            VariableNotFoundError: If the variable represented by this class is not found.

        Example:
        >>> from pythonite_engine.variable import VariableAssignment
        >>> variable_name = "my_var"
        >>> value = 5
        >>> variable = VariableAssignment(variable_name, value)
        >>> variable.execute()
        """
        scope.set_variable_value(self.variable_name, self.value)
