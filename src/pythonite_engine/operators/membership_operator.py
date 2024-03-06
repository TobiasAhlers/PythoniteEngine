from typing import Any, ClassVar, Literal
from pydantic import Field

from ..pythonite_representation import PythoniteRepresentation

from .base import OperatorRepresentation


class MembershipOperatorRepresentation(OperatorRepresentation):
    """
    Represents a membership operator in the Pythonite engine.

    Attributes:
        operator (str): The membership operator that the object represents.
        operands (list[Any]): The operands that the operator operates on.
    """

    __pythonite_signature__: ClassVar[str] = "MembershipOperator"

    operator: Literal["in", "not in"]
    operands: list[Any] = Field(..., min_length=2, max_length=2)

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        for i, operand in enumerate(self.operands):
            if isinstance(operand, PythoniteRepresentation):
                self.operands[i] = operand.execute(*args, **kwargs)
        match self.operator:
            case "in":
                return self.operands[0] in self.operands[1]
            case "not in":
                return self.operands[0] not in self.operands[1]
            case _:
                raise NotImplementedError(
                    f"Expected the operator to be one of 'in', 'not in', but got {self.operator}. This should not happen. Please report this as a bug."
                )
