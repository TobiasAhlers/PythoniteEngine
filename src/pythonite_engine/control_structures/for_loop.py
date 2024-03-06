from typing import ClassVar, Iterable, Any

from ..scope import Scope
from ..pythonite_representation import PythoniteRepresentation
from ..annotation import Annotation
from ..utils import execute_representations

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

    loop_variable_name: str | PythoniteRepresentation
    iterable: PythoniteRepresentation | Iterable
    loop_variable_annotation: Annotation
    body: list[PythoniteRepresentation]

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        iterable = execute_representations(self.iterable, scope=scope, *args, **kwargs)
        loop_variable_name = execute_representations(self.loop_variable_name, scope=scope, *args, **kwargs)

        loop_scope = Scope(parent=scope)
        loop_scope.declare_variable(variable_name=loop_variable_name, type=self.loop_variable_annotation.type)
        
        result = ""
        for item in iterable:
            if isinstance(item, PythoniteRepresentation):
                item = item.execute(scope=scope, *args, **kwargs)
            loop_scope.set_variable_value(variable_name=loop_variable_name, value=item)

            for element in self.body:
                result += str(element.execute(scope=loop_scope, *args, **kwargs))

        return result