from typing import ClassVar, Any, Optional

from ..pythonite_representation import PythoniteRepresentation
from ..operators import OperatorRepresentation
from ..scope import Scope

from .base import ControlStructureRepresentation


class ConditionalStatement(ControlStructureRepresentation):
    """
    Represents a conditional statement in the Pythonite engine.

    Attributes:
        condition (OperatorRepresentation): The condition to check.
        consequent (Any): The action to execute if the condition is true.
        alternate (Optional[Any]): The action to execute if the condition is false.
    """

    __pythonite_signature__: ClassVar[str] = "ConditionalStatement"

    condition: OperatorRepresentation
    consequent: Any
    alternate: Optional[Any] = None

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        if self.condition.execute(scope=scope, *args, **kwargs):
            if isinstance(self.consequent, PythoniteRepresentation):
                return self.consequent.execute(scope=scope, *args, **kwargs)
            else:
                return self.consequent
        else:
            if self.alternate is not None:
                if isinstance(self.alternate, PythoniteRepresentation):
                    return self.alternate.execute(scope=scope, *args, **kwargs)
                else:
                    return self.alternate
