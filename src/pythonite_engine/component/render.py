from typing import ClassVar, Any, TYPE_CHECKING

from ..scope import Scope
from ..pythonite_representation import PythoniteRepresentation

if TYPE_CHECKING:
    from ..pythonite_engine import PythoniteEngine


class RenderComponent(PythoniteRepresentation):
    """
    Represents a render component in the Pythonite engine.

    Attributes:
        args (dict[str, Any]): The arguments to use for the rendering.
    """

    __pythonite_signature__: ClassVar[str] = "RenderComponent"

    component_id: str
    args: dict[str, Any] = {}

    def render(self, scope: Scope, engine: "PythoniteEngine", *args, **kwargs) -> str:
        """
        Render the component represented by this class.

        Returns:
            str: The rendered component.
        """
        return engine.get_component(component_id=self.component_id).render(
            scope=scope, engine=engine, *args, **kwargs | self.args
        )

    def execute(self, scope: Scope, engine: "PythoniteEngine", *args, **kwargs) -> str:
        """
        Render the component represented by this class.

        Args:
            scope (Scope): The scope used as a parent scope for the rendering.

        Returns:
            str: The rendered component.
        """
        return self.render(scope=scope, engine=engine, *args, **kwargs)
