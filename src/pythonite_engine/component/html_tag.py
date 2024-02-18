from typing import ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class HtmlTag(PythoniteRepresentation):
    """
    Represents an HTML tag in the Pythonite engine.

    Attributes:
        tag_name (str): The name of the tag.
        attributes (dict[str, str]): The attributes of the tag.
        content (list[PythoniteRepresentation]): The content of the tag.
    """

    __pythonite_signature__: ClassVar[str] = "HtmlTag"

    tag_name: str
    attributes: dict[str, str]
    content: list[PythoniteRepresentation]

    def render(self, *args, **kwargs) -> str:
        """
        Render the HTML tag represented by this class.

        Returns:
            str: The rendered HTML tag.
        """
        raise NotImplementedError()

    def execute(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the HTML tag represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered HTML tag.
        """
        return self.render(scope, *args, **kwargs)
