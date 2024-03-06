from pydantic import BaseModel
from jinja2 import Template

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
    jinja2_template: str

    def render(self, **args) -> str:
        """
        Render the component represented by this class.

        Attributes:
            args (dict[str, Any]): The arguments to use for the rendering.

        Returns:
            str: The rendered component.
        """
        context = {}
        for arg, annotation in self.annotation.items():
            context[arg] = annotation.validate_annotation(value=args.get(arg, None))
        return Template(source=self.jinja2_template).render(**context)
