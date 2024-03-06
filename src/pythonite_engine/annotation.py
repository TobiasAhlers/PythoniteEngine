from typing import Optional, Any, ClassVar

from .utils import execute_representations
from .scope import Scope
from .pythonite_representation import PythoniteRepresentation
from .types.base import TypeRepresentation
from .errors import ConversionError


class Annotation(PythoniteRepresentation):
    """
    Represents an annotation in the Pythonite engine.

    Attributes:
        type (TypeRepresentation): The type of the annotation.
        default (Any): The default value of the annotation.
        required (bool): Whether the annotation is required or not.
    """

    __pythonite_signature__: ClassVar[str] = "Annotation"

    type: TypeRepresentation
    default: Optional[Any] = None
    required: bool = False

    def validate_annotation(self, value: Any = None, *args, **kwargs) -> Any:
        """
        Validate the annotation value.

        Args:
            value (Any): The value to validate.

        Returns:
            Any: The validated value.

        Raises:
            ConversionError: If the value cannot be converted to the type of the annotation.
        """
        default = execute_representations(self.default, *args, **kwargs)
        required = execute_representations(self.required, *args, **kwargs)

        if value is None:
            if required:
                raise ConversionError(
                    f"Annotation {self.type} is required and cannot be None."
                )
            if default is not None:
                return self.type.convert_value(default)
            return None

        return self.type.convert_value(value)

    def execute(self, scope: Scope, value: Any = None, *args, **kwargs) -> Any:
        """
        Execute the annotation represented by this class.

        Returns:
            Any: The value of the annotation represented by this class.
        """
        return self.validate_annotation(value=value, scope=scope, *args, **kwargs)
