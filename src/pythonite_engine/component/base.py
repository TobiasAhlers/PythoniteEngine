from pydantic import BaseModel

from ..scope import Scope
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
        jinja2_template (str): The template of the component.
    """

    component_id: str
    annotation: dict[str, Annotation] = {}
    content: list[PythoniteRepresentation] = []

    def render(self, scope: Scope, **args) -> str:
        """
        Render the component represented by this class.

        Attributes:
            args (dict[str, Any]): The arguments to use for the rendering.

        Returns:
            str: The rendered component.
        """
        component_scope = Scope(parent=scope)
        for arg, annotation in self.annotation.items():
            component_scope.declare_variable(variable_name=arg, type=annotation.type)
            component_scope.set_variable_value(variable_name=arg, value=args.get(arg, None))
        html = ""
        for content in self.content:
            html += str(content.execute(scope=component_scope))
        return html
