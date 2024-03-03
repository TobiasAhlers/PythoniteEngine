from typing import Any, ClassVar

from ..scope import Scope
from ..errors import ConversionError

from .base import TypeRepresentation


class NoneTypeRepresentation(TypeRepresentation):
    """
    Represents a NoneType in the PythoniteEngine.
    """

    __pythonite_signature__: ClassVar[str] = "NoneType"

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
        if value is None:
            return None
        raise ConversionError(f"Could not convert {value} to None.")

    def get_type(self) -> type:
        """
        Get the type represented by this class.

        Returns:
            type: The type represented by this class.
        """
        return type(None)

    def execute(self, value: Any, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the value represented by this class.

        Args:
            value (Any): The value to execute.
            scope (Scope): The scope in which to execute the value.
            *args: Any positional arguments to pass to the value.
            **kwargs: Any keyword arguments to pass to the value.
        """
        return None
