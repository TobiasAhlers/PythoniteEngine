from typing import Any, ClassVar

from ..pythonite_representation import PythoniteRepresentation

from .base import OperatorRepresentation


class IndexAccessOperatorRepresentation(OperatorRepresentation):
    """
    Represents an index access operator in the Pythonite engine.
    """

    __pythonite_signature__: ClassVar[str] = "IndexAccessOperator"

    index: str | int
    operands: dict | list

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        operands = self.operands
        if isinstance(operands, list):
            for i, operand in enumerate(operands):
                if isinstance(operand, PythoniteRepresentation):
                    operands[i] = operand.execute(*args, **kwargs)
        elif isinstance(operands, dict):
            for key, operand in operands.items():
                if isinstance(operand, PythoniteRepresentation):
                    operands[key] = operand.execute(*args, **kwargs)
        return self.operands[self.index]
