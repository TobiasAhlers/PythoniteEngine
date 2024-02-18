from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class VariableRepresentation(PythoniteRepresentation):
    """
    Represents a variable in the Pythonite engine.

    This class is an abstract class that should be inherited by all variable representations.
    The subclasses should implement the `execute` method.

    Attributes:
        variable_name (str): The name of the variable represented by this class.
    """

    variable_name: str

    def execute(self, scope: Scope, *args, **kwargs) -> None:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.

        Raises:
            VariableError: If the action represented by this class fails.
        """
        raise NotImplementedError(
            f"Expected subclass of VariableRepresentation {self.__class__.__name__} to implement execute method."
        )
