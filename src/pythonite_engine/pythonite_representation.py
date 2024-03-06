from typing_extensions import Literal
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar

from .scope import Scope


class PythoniteRepresentation(BaseModel):
    """
    Represents a Pythonite representation.

    This class is intended to be subclassed to create custom representations for the Pythonite engine.
    The subclass should override the __pythonite_signature__ attribute to provide a signature for the representation
    with which it can be identified.

    Example:
    >>> from pythonite_engine.pythonite_representation import PythoniteRepresentation
    >>> class MyRepresentation(PythoniteRepresentation):
    ...     __pythonite_signature__ = "MyRepresentation"
    ...
    >>> MyRepresentation.__pythonite_signature__
    'MyRepresentation'
    """

    __pythonite_signature__: ClassVar[str]

    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=False)

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        raise NotImplementedError(
            f"Expected subclass of PythoniteRepresentation {self.__class__.__name__} to implement execute method."
        )

    def model_dump(self) -> dict[str, Any]:
        """
        Dump the PythoniteRepresentation instance to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the PythoniteRepresentation instance.
        """
        items = {}
        for key, value in self.__dict__.items():
            if key == "model_config":
                continue
            if isinstance(value, PythoniteRepresentation):
                items[key] = value.model_dump()
            elif isinstance(value, list):
                elements = []
                for element in value:
                    if isinstance(element, PythoniteRepresentation):
                        elements.append(element.model_dump())
                    else:
                        elements.append(element)
                items[key] = elements
            elif isinstance(value, dict):
                elements = {}
                for k, v in value.items():
                    if isinstance(v, PythoniteRepresentation):
                        elements[k] = v.model_dump()
                    else:
                        elements[k] = v
                items[key] = elements
            else:
                items[key] = value
        items["__pythonite_signature__"] = self.__pythonite_signature__

        return items
