from typing import Any, ClassVar

from ..errors import ConversionError

from .base import TypeRepresentation
from .any_type import AnyTypeRepresentation


class ListTypeRepresentation(TypeRepresentation):
    """
    Represents a ListType in the PythoniteEngine.
    """

    __pythonite_signature__: ClassVar[str] = "ListType"

    allowed_types: list[TypeRepresentation] = [AnyTypeRepresentation()]

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
        try:
            return_list = []
            for element in list(value):
                for allowed_type in self.allowed_types:
                    return_list.append(allowed_type.convert_value(element))
            return return_list

        except (ValueError, TypeError):
            raise ConversionError(f"Could not convert {value} to list.")

    def get_type(self) -> type:
        """
        Get the type represented by this class.

        Returns:
            type: The type represented by this class.
        """
        return list
