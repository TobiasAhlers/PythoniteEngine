from typing import ClassVar, Iterable

from ..scope import Scope
from ..pythonite_representation import PythoniteRepresentation

from .base import ControlStructureRepresentation


class ForLoop(ControlStructureRepresentation):
    """
    Represents a for loop in the Pythonite engine.

    Attributes:
        loop_variable_name (str): The name of the loop variable.
        iterable (Iterable): The iterable to loop through.
        body (Any): The body of the for loop.
    """

    __pythonite_signature__: ClassVar[str] = "ForLoop"

    loop_variable_name: str
    iterable: Iterable
    body: list[PythoniteRepresentation]

    def execute(self, scope: Scope, *args, **kwargs) -> None:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        raise NotImplementedError()
