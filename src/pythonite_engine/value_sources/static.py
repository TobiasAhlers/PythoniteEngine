from typing import ClassVar, Any

from ..types.base import TypeRepresentation
from ..scope import Scope

from .base import ValueSource


class StaticValue(ValueSource):
    """
    Represents a static value. A static value is a value that does not change and is always the same.

    Attributes:
        type (TypeRepresentation): The type of the static value.
        value (Any): The value of the static value.

    Example:
    >>> from pythonite_engine.value_sources import StaticValue
    >>> static_value = StaticValue(type=IntegerType(), value=5)
    >>> static_value.execute()
    5
    """

    __pythonite_signature__: ClassVar[str] = "StaticValue"

    type: TypeRepresentation
    value: Any

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the static value represented by this class.

        Returns:
            Any: The value of the static value represented by this class.

        Example:
        >>> from pythonite_engine.value_sources import StaticValue
        >>> static_value = StaticValue(type=IntegerType(), value=5)
        >>> static_value.execute()
        5
        """
        return self.value
