from typing import ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class TemplateChildren(PythoniteRepresentation):
    """
    Represents the children of a PythoniteTemplate.

    This class is used to represent the children of a PythoniteTemplate. It is used to represent the children of a
    PythoniteTemplate in a way that can be rendered.

    Attributes:
        content (list[PythoniteRepresentation]): The children of the PythoniteTemplate.
    """

    __pythonite_signature__: ClassVar[str] = "Children"

    content: list[PythoniteRepresentation] = []

    def render(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the children represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered children.
        """
        result = ""
        for child in self.content:
            result += str(child.execute(scope=scope, *args, **kwargs))
        return result

    def execute(self, scope: Scope, *args, **kwargs) -> str:
        return self.render(scope=scope, *args, **kwargs)
