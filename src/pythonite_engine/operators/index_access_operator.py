from typing import Any, ClassVar

from ..utils import execute_representations
from ..errors import OperatorError
from ..pythonite_representation import PythoniteRepresentation

from .base import OperatorRepresentation


class IndexAccessOperatorRepresentation(OperatorRepresentation):
    """
    Represents an index access operator in the Pythonite engine.
    """

    __pythonite_signature__: ClassVar[str] = "IndexAccessOperator"

    index: str | int | PythoniteRepresentation
    operands: dict | list | PythoniteRepresentation

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        operands = execute_representations(self.operands, *args, **kwargs)
        index = execute_representations(self.index, *args, **kwargs)

        try:
            return operands[index]
        except (KeyError, IndexError, TypeError):
            raise OperatorError(
                f"Index access operator {index} is not valid for {operands}."
            )
