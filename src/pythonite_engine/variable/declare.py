from typing import Literal, ClassVar

from ..types.base import TypeRepresentation
from ..scope import Scope
from ..utils import execute_representations

from .base import VariableRepresentation


class VariableDeclaration(VariableRepresentation):
    """
    Represents a variable declaration in the Pythonite engine.

    Attributes:
        variable_name (str): The name of the variable declared.
        type (TypeRepresentation): The type of the variable declared.
        scope (Literal["global", "local"]): The scope of the variable declared.
    """

    __pythonite_signature__: ClassVar[str] = "VariableDeclaration"

    type: TypeRepresentation
    scope: Literal["global", "local"]

    def execute(self, scope: Scope, *args, **kwargs) -> None:
        """
        Execute the variable declaration represented by this class.

        Args:
            scope (Scope): The scope to use for the declaration.

        Raises:
            VariableAlreadyDeclaredError: If the variable represented by this class is already declared.

        Example:
        >>> from pythonite_engine.variable import VariableDeclaration
        >>> from pythonite_engine.types import TypeRepresentation
        >>> variable_name = "my_var"
        >>> type = TypeRepresentations()
        >>> scope = "local"
        >>> variable = VariableDeclaration(variable_name, type, scope)
        >>> variable.execute()
        """
        variable_name = execute_representations(self.variable_name, scope=scope, *args, **kwargs)
        variable_scope = execute_representations(self.scope, scope=scope, *args, **kwargs)

        scope.declare_variable(
            variable_name=variable_name, type=self.type, scope=variable_scope
        )
