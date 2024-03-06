from typing import Any, ClassVar, Literal
from pydantic import Field

from ..utils import execute_representations

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

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        operator = execute_representations(self.operator, *args, **kwargs)
        operands = execute_representations(self.operands, *args, **kwargs)
        
        match operator:
            case "and":
                return all(operands)
            case "or":
                return any(operands)
            case _:
                raise NotImplementedError(
                    f"Expected the operator to be one of 'and', 'or', but got {operator}. This should not happen. Please report this as a bug."
                )
