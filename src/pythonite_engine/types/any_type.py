from typing import Any, ClassVar

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
