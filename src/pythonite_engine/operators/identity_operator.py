from typing import Any, ClassVar, Literal
from pydantic import Field

from ..utils import execute_representations

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
        operator = execute_representations(self.operator, *args, **kwargs)
        operands = execute_representations(self.operands, *args, **kwargs)

        match operator:
            case "is":
                return operands[0] is operands[1]
            case "is not":
                return operands[0] is not operands[1]
            case _:
                raise NotImplementedError(
                    f"Expected the operator to be one of 'is', 'is not', but got {operator}. This should not happen. Please report this as a bug."
                )
