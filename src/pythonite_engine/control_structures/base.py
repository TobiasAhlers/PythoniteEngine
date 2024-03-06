from typing import ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class ControlStructureRepresentation(PythoniteRepresentation):
    """
    Represents a control structure in the Pythonite engine.

    This class is an abstract class that should be inherited by all control structure representations.
    The subclasses should implement the `execute` method.
    """

    __pythonite_signature__: ClassVar[str]

    def execute(self, scope: Scope, *args, **kwargs) -> None:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        raise NotImplementedError(
            f"Expected subclass {self.__class__.__name__} of ControlStructureRepresentation to implement execute method."
        )
