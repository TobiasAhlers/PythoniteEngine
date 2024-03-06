from typing import ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class ValueSource(PythoniteRepresentation):
    """
    Represents a value source in the Pythonite engine.

    This class is intended to be subclassed to create custom value sources for the Pythonite engine.
    The subclass should override the execute method to provide the functionality of the value source and
    the __pythonite_signature__ attribute to provide a signature for the representation with which it can be identified.

    Example:
    >>> from pythonite_engine.value_sources import ValueSource
    >>> class MyValueSource(ValueSource):
    ...     __pythonite_signature__: ClassVar[str] = "MyValueSource"
    ...
    ...     def execute(self, scope: Scope, *args, **kwargs):
    ...         return 5
    ...
    >>> MyValueSource().execute()
    5
    """

    __pythonite_signature__: ClassVar[str]

    def execute(self, scope: Scope, *args, **kwargs):
        """
        Execute the value source represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.

        Returns:
            Any: The result of executing the value source represented by this class.

        Example:
        >>> from pythonite_engine.value_sources import ValueSource
        >>> class MyValueSource(ValueSource):
        ...     __pythonite_signature__: ClassVar[str] = "MyValueSource"
        ...
        ...     def execute(self, scope: Scope, *args, **kwargs):
        ...         return 5
        ...
        >>> MyValueSource().execute()
        5
        """
        raise NotImplementedError(
            f"Expected subclass {self.__class__.__name__} of ValueSource to implement execute method."
        )
