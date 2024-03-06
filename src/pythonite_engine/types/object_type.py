from typing import Any, ClassVar, Self
from pydantic import model_validator

from ..errors import ConversionError

from .base import TypeRepresentation


class ObjectTypeRepresentation(TypeRepresentation):
    """
    Represents an ObjectType in the PythoniteEngine.
    """

    __pythonite_signature__: ClassVar[str] = "ObjectType"

    properties: dict[str, TypeRepresentation] = {}
    defaults: dict[str, Any] = {}
    required: list[str] = []

    @model_validator(mode="after")
    def validate_defaults(self) -> Self:
        """
        Validate the defaults.

        Returns:
            Self: The instance of the class.
        """
        for key, value in self.defaults.items():
            if key not in self.properties:
                raise ValueError(f"Default value for non-existent property {key}.")
            try:
                self.properties[key].convert_value(value)
            except ConversionError as e:
                raise ValueError(f"Default value for property {key} is invalid: {e}.")
        return self

    @model_validator(mode="after")
    def validate_required(self) -> Self:
        """
        Validate the required properties.

        Returns:
            Self: The instance of the class.
        """
        for key in self.required:
            if key not in self.properties:
                raise ValueError(f"Required property {key} does not exist.")
        return self

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
            value = dict(value)
            return_value = {}
            for key, type_ in self.properties.items():
                if key in value:
                    return_value[key] = type_.convert_value(value[key])
                elif key in self.defaults:
                    return_value[key] = self.defaults[key]
                else:
                    raise ConversionError(f"Missing required property {key}.")
            return return_value
        except (ValueError, TypeError):
            raise ConversionError(
                f"Could not convert {value} to object of type {self}."
            )

    def get_type(self) -> type:
        """
        Get the type represented by this class.

        Returns:
            type: The type represented by this class.
        """
        return dict
