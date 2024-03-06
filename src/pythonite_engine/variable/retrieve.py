from typing import Any, ClassVar

from ..scope import Scope
from ..utils import execute_representations

from .base import VariableRepresentation


class VariableRetrieval(VariableRepresentation):
    """
    Represents a variable value retrieval in the Pythonite engine.

    Attributes:
        variable_name (str): The name of the variable declared.
    """

    __pythonite_signature__: ClassVar[str] = "VariableRetrieval"

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Retrieve the value of the variable represented by this class.

        Args:
            scope (Scope): The scope to use for the retrieval.

        Returns:
            Any: The value of the variable represented by this class.

        Raises:
            VariableNotFoundError: If the variable represented by this class is not found.

        Example:
        >>> from pythonite_engine.variable import VariableRetrieval
        >>> variable_name = "my_var"
        >>> variable = VariableRetrieval(variable_name)
        >>> variable.execute()
        5
        """
        variable_name = execute_representations(self.variable_name, scope=scope, *args, **kwargs)

        return scope.get_variable_value(variable_name)
