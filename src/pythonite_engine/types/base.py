from typing import Any, ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope
from ..utils import execute_representations


class TypeRepresentation(PythoniteRepresentation):
    """
    Represents an enforced type hint in the Pythonite engine.

    This class is intended to be subclassed to create custom type representations for the Pythonite engine.
    The subclass should implement the convert_value method to convert values to the type represented by the subclass.

    Example:
    >>> from pythonite_engine.type_representations import TypeRepresentation
    >>> class MyTypeRepresentation(TypeRepresentation):
    ...     __pythonite_signature__: ClassVar[str] = "MyTypeRepresentation"
    ...     def convert_value(self, value):
    ...         try:
    ...             return int(value)
    ...         except ValueError:
    ...             raise ConversionError(f"Could not convert {value} to int.")
    ...
    ...     def get_type(self):
    ...         return int
    ...
    >>> MyTypeRepresentation().convert_value("5")
    5
    """

    __pythonite_signature__: ClassVar[str]

    def convert_value(self, value: Any) -> Any:
        """
        Convert the value to the type represented by this class.

        Args:
            value (Any): The value to convert.

        Returns:
            Any: The value converted to the type represented by this class.

        Raises:
            ConversionError: If the value cannot be converted to the type represented by this class.

        Example:
        >>> from pythonite_engine.type_representations import TypeRepresentation
        >>> class MyTypeRepresentation(TypeRepresentation):
        ...     def convert_value(self, value):
        ...         return int(value)
        ...
        >>> MyTypeRepresentation().convert_value("5")
        5
        """
        raise NotImplementedError(
            f"Expected subclass {self.__class__.__name__} of TypeRepresentation to implement convert_value method."
        )

    def get_type(self) -> type:
        """
        Get the type represented by this class.

        Returns:
            type: The type represented by this class.

        Example:
        >>> from pythonite_engine.type_representations import TypeRepresentation
        >>> class MyTypeRepresentation(TypeRepresentation):
        ...     def get_type(self):
        ...         return int
        ...
        >>> MyTypeRepresentation().get_type()
        <class 'int'>
        """

        raise NotImplementedError(
            f"Expected subclass {self.__class__.__name__} of TypeRepresentation to implement get_type method."
        )

    def execute(self, value: Any, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the action represented by this class.

        Args:
            value (Any): The value to convert to the type represented by this class.
            scope (Scope): The scope to use as a parent for the execution.

        Raises:
            TypeError: If the action represented by this class fails.

        Example:
        >>> from pythonite_engine.type_representations import TypeRepresentation
        >>> class MyTypeRepresentation(TypeRepresentation):
        ...     def convert_value(self, value):
        ...         return int(value)
        ...
        >>> MyTypeRepresentation().execute()
        """
        value = execute_representations(value, scope=scope, *args, **kwargs)

        return self.convert_value(value)
