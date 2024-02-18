from pydantic import BaseModel
from typing import Self

from ..pythonite_representation import PythoniteRepresentation
from ..annotation import Annotation


class Component(BaseModel):
    """
    Represents a component in the Pythonite engine.

    This class is an abstract class that should be inherited by all component representations.
    The subclasses should implement the `execute` method.

    Attributes:
        component_id (str): The id of the component.
        annotation (dict[str, Annotation]): The annotations of the component.
        content (list[PythoniteRepresentation]): The content of the component.
    """

    component_id: str
    annotation: dict[str, Annotation] = {}
    content: list[PythoniteRepresentation]

    @classmethod
    def from_jinja2(cls: Self, jinja2: str, *args, **kwargs) -> Self:
        """
        Create a new instance of this class from a Jinja2 template.

        Args:
            jinja2 (str): The Jinja2 template to use for the creation.

        Returns:
            Self: The new instance of this class.
        """
        raise NotImplementedError()

    def render(self, **args) -> str:
        """
        Render the component represented by this class.

        Attributes:
            args (dict[str, Any]): The arguments to use for the rendering.

        Returns:
            str: The rendered component.
        """
        raise NotImplementedError()
