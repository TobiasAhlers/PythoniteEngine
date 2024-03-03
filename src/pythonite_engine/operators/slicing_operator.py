from typing import Any, ClassVar, Optional

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

    def execute(self) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        return self.operands[slice(self.start, self.stop, self.step)]
