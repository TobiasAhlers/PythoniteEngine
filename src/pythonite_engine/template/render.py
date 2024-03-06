from typing import ClassVar, TYPE_CHECKING

from ..pythonite_representation import PythoniteRepresentation
from ..utils import execute_representations
from ..scope import Scope

if TYPE_CHECKING:
    from ..pythonite_engine import PythoniteEngine


class RenderTemplate(PythoniteRepresentation):
    """
    Represents a template in the Pythonite engine that will be rendered on execution

    Attributes:
        template_id (str): The id of the template represented by this class.
        content (list[TemplateBlock]): The content of the template represented by this class.
    """

    __pythonite_signature__: ClassVar[str] = "RenderTemplate"

    template_id: str | PythoniteRepresentation

    def render(self, scope: Scope, engine: "PythoniteEngine", *args, **kwargs) -> str:
        """
        Render the template represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered template.
        """
        template_id = execute_representations(
            self.template_id, scope=scope, *args, **kwargs
        )
        return engine.get_template(template_id=template_id).render(
            global_scope=scope, engine=engine, *args, **kwargs
        )

    def execute(self, scope: Scope, engine: "PythoniteEngine", *args, **kwargs) -> str:
        """
        Render the template represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered template.
        """
        return self.render(scope=scope, engine=engine, *args, **kwargs)
