from typing import Optional, Any, ClassVar

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

    def validate_annotation(self, value: Any, *args, **kwargs) -> Any:
        """
        Validate the annotation value.

        Args:
            value (Any): The value to validate.

        Returns:
            Any: The validated value.

        Raises:
            ConversionError: If the value cannot be converted to the type of the annotation.
        """
        raise NotImplementedError()

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the annotation represented by this class.

        Returns:
            Any: The value of the annotation represented by this class.
        """
        return self.validate_annotation(self.default, *args, **kwargs)
