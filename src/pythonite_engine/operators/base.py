from typing import Any, ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class OperatorRepresentation(PythoniteRepresentation):
    """
    Represents an operator in the Pythonite engine.

    This class is intended to be subclassed to create custom operator representations for the Pythonite engine.
    The subclass should override the execute method to provide the functionality of the operator and
    the __pythonite_signature__ attribute to provide a signature for the representation with which it can be identified.

    Attributes:
        operator (str): The operator represented by this class.
        operands (list[Any]): The operands of the operator represented by this class.

    Example:
    >>> from pythonite_engine.operators import OperatorRepresentation
    >>> class MyOperatorRepresentation(OperatorRepresentation):
    ...     __pythonite_signature__: ClassVar[str] = "MyOperatorRepresentation"
    ...     operator: Literal["+"]
    ...     operands: list[Any]
    ...
    ...     def execute(self):
    ...         return self.operands[0] + self.operands[1]
    ...
    >>> MyOperatorRepresentation(operator="+", operands=[5, 3]).execute()
    8
    """

    __pythonite_signature__: ClassVar[str]

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the operator represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        
        Returns:
            Any: The result of executing the operator represented by this class.

        Example:
        >>> from pythonite_engine.operators import OperatorRepresentation
        >>> class MyOperatorRepresentation(OperatorRepresentation):
        ...     __pythonite_signature__: ClassVar[str] = "MyOperatorRepresentation"
        ...     operator: Literal["+"]
        ...     operands: list[Any]
        ...
        ...     def execute(self):
        ...         return self.operands[0] + self.operands[1]
        ...
        >>> MyOperatorRepresentation(operator="+", operands=[5, 3]).execute()
        8
        """
        raise NotImplementedError(
            f"Expected subclass {self.__class__.__name__} of OperatorRepresentation to implement execute method."
        )
