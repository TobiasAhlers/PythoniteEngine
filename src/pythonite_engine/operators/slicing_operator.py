from typing import Any, ClassVar, Optional

from ..pythonite_representation import PythoniteRepresentation

from .base import OperatorRepresentation


class SlicingOperatorRepresentation(OperatorRepresentation):
    """
    Represents a slicing operator in the Pythonite engine.
    """

    __pythonite_signature__: ClassVar[str] = "SlicingOperator"

    start: Optional[int] = None
    stop: Optional[int] = None
    step: Optional[int] = None

    operands: list

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        operands = self.operands
        for i, operand in enumerate(operands):
            if isinstance(operand, PythoniteRepresentation):
                operands[i] = operand.execute(*args, **kwargs)
        return operands[slice(self.start, self.stop, self.step)]
