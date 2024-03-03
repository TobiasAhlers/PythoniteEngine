from typing import Any, ClassVar

from ..scope import Scope

from .base import TypeRepresentation


class AnyTypeRepresentation(TypeRepresentation):
    """
    Represents a AnyType in the PythoniteEngine.
    """

    __pythonite_signature__: ClassVar[str] = "AnyType"

    def convert_value(self, value: Any) -> Any:
        """
        Convert the value to the type represented by this class.

        Args:
            value (Any): The value to convert.

        Returns:
            Any: The value converted to the type represented by this class.

        Raises:
            ConversionError: If the value cannot be converted to the type represented by this class.
        """
        return value

    def get_type(self) -> type:
        """
        Get the type represented by this class.

        Returns:
            type: The type represented by this class.
        """
        return Any

    def execute(self, value: Any, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the value represented by this class.

        Args:
            value (Any): The value to execute.
            scope (Scope): The scope in which to execute the value.
            *args: Any positional arguments to pass to the value.
            **kwargs: Any keyword arguments to pass to the value.

        Returns:
            Any: The result of executing the value.
        """
        return self.convert_value(value)
