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
    attributes: dict[str, str | bool] = {}
    classes: list[str] = []
    styles: dict[str, str] = {}
    content: list[PythoniteRepresentation] = []

    def render_classes(self) -> str:
        """
        Render the classes of the tag represented by this class.

        Returns:
            str: The rendered classes.
        """
        classes = " ".join(self.classes)
        return f' class="{classes}"' if classes else ""
    
    def render_styles(self) -> str:
        """
        Render the styles of the tag represented by this class.

        Returns:
            str: The rendered styles.
        """
        styles = ";".join(
            [f"{style_name}: {style_value}" for style_name, style_value in self.styles.items()]
        )
        return f' style="{styles}"' if styles else ""

    def render_attributes(self) -> str:
        """
        Render the attributes of the tag represented by this class.

        Returns:
            str: The rendered attributes.
        """
        attributes = " ".join(
            [
                (
                    f'{attribute_name}="{attribute_value}"'
                    if isinstance(attribute_value, str)
                    else f"{attribute_name}"
                )
                for attribute_name, attribute_value in self.attributes.items()
            ]
        )
        return f" {attributes}" if attributes else ""

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
        return f"<{self.tag_name}{self.render_classes()}{self.render_styles()}{self.render_attributes()}>{self.render_content(scope, *args, **kwargs)}</{self.tag_name}>"

    def execute(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the HTML tag represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered HTML tag.
        """
        return self.render(scope, *args, **kwargs)
