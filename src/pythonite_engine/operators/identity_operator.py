from typing import Any, ClassVar, Literal
from pydantic import Field

from ..pythonite_representation import PythoniteRepresentation

from .base import OperatorRepresentation


class IdentityOperatorRepresentation(OperatorRepresentation):
    """
    Represents an identity operator in the Pythonite engine.

    Attributes:
        operator (str): The identity operator that the object represents.
        operands (list[Any]): The operands that the operator operates on.
    """

    __pythonite_signature__: ClassVar[str] = "IdentityOperator"

    operator: Literal["is", "is not"]
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
            case "is":
                return self.operands[0] is self.operands[1]
            case "is not":
                return self.operands[0] is not self.operands[1]
            case _:
                raise NotImplementedError(
                    f"Expected the operator to be one of 'is', 'is not', but got {self.operator}. This should not happen. Please report this as a bug."
                )
