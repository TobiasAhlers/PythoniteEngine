from typing import Any, ClassVar, Optional

from ..utils import execute_representations
from ..pythonite_representation import PythoniteRepresentation

from .base import OperatorRepresentation


class SlicingOperatorRepresentation(OperatorRepresentation):
    """
    Represents a slicing operator in the Pythonite engine.
    """

    __pythonite_signature__: ClassVar[str] = "SlicingOperator"

    start: Optional[int | PythoniteRepresentation] = None
    stop: Optional[int | PythoniteRepresentation] = None
    step: Optional[int | PythoniteRepresentation] = None

    operands: list

    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Returns:
            Any: The result of executing the operator represented by this class.
        """
        self.operands = execute_representations(self.operands, *args, **kwargs)
        self.start = execute_representations(self.start, *args, **kwargs)
        self.stop = execute_representations(self.stop, *args, **kwargs)
        self.step = execute_representations(self.step, *args, **kwargs)

        return self.operands[slice(self.start, self.stop, self.step)]
