from typing import ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope
from ..utils import execute_representations


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
    attributes: dict[str, str | bool] = {}
    classes: list[str] = []
    styles: dict[str, str] = {}
    content: list[PythoniteRepresentation] = []

    def render_classes(self, *args, **kwargs) -> str:
        """
        Render the classes of the tag represented by this class.

        Returns:
            str: The rendered classes.
        """
        classes = execute_representations(self.classes, *args, **kwargs)
        html = " ".join(classes)
        return f' class="{html}"' if html else ""

    def render_styles(self, *args, **kwargs) -> str:
        """
        Render the styles of the tag represented by this class.

        Returns:
            str: The rendered styles.
        """
        styles = execute_representations(self.styles, *args, **kwargs)
        html = ";".join(
            [
                f"{style_name}: {style_value}"
                for style_name, style_value in styles.items()
            ]
        )
        return f' style="{html}"' if html else ""

    def render_attributes(self, *args, **kwargs) -> str:
        """
        Render the attributes of the tag represented by this class.

        Returns:
            str: The rendered attributes.
        """
        attributes = execute_representations(self.attributes, *args, **kwargs)
        html = " ".join(
            [
                (
                    f'{attribute_name}="{attribute_value}"'
                    if isinstance(attribute_value, str)
                    else f"{attribute_name}"
                )
                for attribute_name, attribute_value in attributes.items()
            ]
        )
        return f" {html}" if html else ""

    def render_content(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the content of the tag represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered content.
        """
        return "".join(
            [child.execute(scope, *args, **kwargs) for child in self.content]
        )

    def render(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the HTML tag represented by this class.

        Returns:
            str: The rendered HTML tag.
        """
        return f"<{self.tag_name}{self.render_classes(scope=scope, *args, **kwargs)}{self.render_styles(scope=scope, *args, **kwargs)}{self.render_attributes(scope=scope, *args, **kwargs)}>{self.render_content(scope, *args, **kwargs)}</{self.tag_name}>"

    def execute(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the HTML tag represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered HTML tag.
        """
        return self.render(scope, *args, **kwargs)
