from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar

from .scope import Scope


class PythoniteRepresentation(BaseModel):
    """
    Represents a Pythonite representation.

    This class is intended to be subclassed to create custom representations for the Pythonite engine.
    The subclass should override the __pythonite_signature__ attribute to provide a signature for the representation
    with which it can be identified.

    Example:
    >>> from pythonite_engine.pythonite_representation import PythoniteRepresentation
    >>> class MyRepresentation(PythoniteRepresentation):
    ...     __pythonite_signature__ = "MyRepresentation"
    ...
    >>> MyRepresentation.__pythonite_signature__
    'MyRepresentation'
    """

    __pythonite_signature__: ClassVar[str]

    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=False)

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        raise NotImplementedError(
            f"Expected subclass of PythoniteRepresentation {self.__class__.__name__} to implement execute method."
        )
