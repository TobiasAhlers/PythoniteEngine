from typing import Any, ClassVar, Literal
from pydantic import Field

from ..utils import execute_representations

from .base import OperatorRepresentation


class ArithmeticOperatorRepresentation(OperatorRepresentation):
    """
    Represents an arithmetic operator in the Pythonite engine.

    Attributes:
        operator (str): The arithmetic operator that the object represents.
        operands (list[Any]): The operands that the operator operates on.
    """

    __pythonite_signature__: ClassVar[str] = "ArithmeticOperator"

    operator: Literal["+", "-", "*", "/", "//", "%", "**"]
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
            case "+":
                return operands[0] + operands[1]
            case "-":
                return operands[0] - operands[1]
            case "*":
                return operands[0] * operands[1]
            case "/":
                return operands[0] / operands[1]
            case "//":
                return operands[0] // operands[1]
            case "%":
                return operands[0] % operands[1]
            case "**":
                return operands[0] ** operands[1]
            case _:
                raise NotImplementedError(
                    f"Expected the operator to be one of '+', '-', '*', '/', '//', '%', '**', but got {operator}. This should not happen. Please report this as a bug."
                )
