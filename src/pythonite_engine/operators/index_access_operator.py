from typing import Any, ClassVar

from .base import OperatorRepresentation


class IndexAccessOperatorRepresentation(OperatorRepresentation):
    """
    Represents an index access operator in the Pythonite engine.
    """

    __pythonite_signature__: ClassVar[str] = "IndexAccessOperator"

    index: str | int
    operands: dict | list

    def execute(self) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        return self.operands[self.index]
