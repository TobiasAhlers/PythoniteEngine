from typing import Any, ClassVar, Literal
from pydantic import Field

from .base import OperatorRepresentation


class LogicalOperatorRepresentation(OperatorRepresentation):
    """
    Represents an logical operator in the Pythonite engine.

    Attributes:
        operator (str): The logical operator that the object represents.
        operands (list[Any]): The operands that the operator operates on.
    """

    __pythonite_signature__: ClassVar[str] = "LogicalOperator"

    operator: Literal["and", "or"]
    operands: list[Any] = Field(..., min_length=2)

    def execute(self) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        match self.operator:
            case "and":
                return all(self.operands)
            case "or":
                return any(self.operands)
            case _:
                raise NotImplementedError(
                    f"Expected the operator to be one of 'and', 'or', but got {self.operator}. This should not happen. Please report this as a bug."
                )
