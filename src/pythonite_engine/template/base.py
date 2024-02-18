from typing import ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope

from .block import TemplateBlock


class RenderTemplate(PythoniteRepresentation):
    """
    Represents a template in the Pythonite engine that will be rendered on execution

    Attributes:
        template_id (str): The id of the template represented by this class.
        content (list[TemplateBlock]): The content of the template represented by this class.
    """

    __pythonite_signature__: ClassVar[str] = "RenderTemplate"

    template_id: str
    content: list[TemplateBlock]

    def render(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the template represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered template.
        """
        raise NotImplementedError()

    def execute(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the template represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered template.
        """
        return self.render(scope, *args, **kwargs)
