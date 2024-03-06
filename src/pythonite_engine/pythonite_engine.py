from typing import Callable, TYPE_CHECKING

from .pythonite_representation import PythoniteRepresentation
from .scope import Scope

from .variable import *
from .types import *
from .operators import *
from .template import *
from .value_sources import *
from .control_structures import *
from .component import *

from .errors import *

if TYPE_CHECKING:
    from .pythonite_template import PythoniteTemplate


class PythoniteEngine:
    """
    Represents the Pythonite engine.

    This class is the main class of the Pythonite engine. It is responsible for managing the representations of the
    Pythonite engine and for executing the actions represented by the representations. It is also responsible for
    registering and getting functions.

    Attributes:
        representations (dict[str, PythoniteRepresentation]): The representations of the Pythonite engine.
        functions (dict[str, Callable]): The registered functions of the Pythonite engine that can be executed from a
            PythoniteTemplate.
    """

    def __init__(self) -> None:
        self.representations: dict[str, PythoniteRepresentation] = {}
        self.functions: dict[str, Callable] = {}
        self.global_scope = Scope()
        self.components: dict[str,] = {}
        self.templates: dict[str, "PythoniteTemplate"] = {}

    def register_function(self, function_id: str, function: Callable) -> None:
        """
        Register a function with the Pythonite engine. This makes it executable from a PythoniteTemplate.

        Args:
            function_id (str): The id of the function to register.
            function (Callable): The function to register.

        Example:
        >>> from pythonite_engine import PythoniteEngine
        >>> engine = PythoniteEngine()
        >>> engine.register_function("my_function", lambda x: x + 1)
        """
        if function_id in self.functions:
            raise FunctionAlreadyRegisteredError(
                f"Function with id {function_id} already registered in Pythonite engine."
            )
        self.functions[function_id] = function

    def get_function(self, function_id: str) -> Callable:
        """
        Get a registered function from the Pythonite engine.

        Args:
            function_id (str): The id of the function to get.

        Returns:
            Callable: The registered function with the given id.

        Example:
        >>> from pythonite_engine import PythoniteEngine
        >>> engine = PythoniteEngine()
        >>> engine.register_function("my_function", lambda x: x + 1)
        >>> engine.get_function("my_function")
        <function <lambda> at 0x7f1c1b1e6c10>
        """
        try:
            return self.functions[function_id]
        except KeyError:
            raise FunctionNotFoundError(
                f"Function with id {function_id} not found in Pythonite engine."
            )

    def register_representation(self, representation: PythoniteRepresentation) -> None:
        """
        Register a representation with the Pythonite engine. This makes it retrievable from a PythoniteTemplate.

        Args:
            representation (PythoniteRepresentation): The representation to register.
        """
        if representation.__pythonite_signature__ in self.representations:
            raise RepresentationAlreadyRegisteredError(
                f"Representation with id {representation.__pythonite_signature__} already registered in Pythonite engine."
            )
        self.representations[representation.__pythonite_signature__] = representation

    def get_representation(self, pythonite_id: str) -> type[PythoniteRepresentation]:
        """
        Get a representation from the Pythonite engine.

        Args:
            pythonite_id (str): The id of the representation to get.

        Returns:
            type[PythoniteRepresentation]: The representation with the given id.

        Example:
        >>> from pythonite_engine import PythoniteEngine
        >>> from pythonite_engine import PythoniteRepresentation
        >>> class MyRepresentation(PythoniteRepresentation):
        ...     __pythonite_signature__ = "my_representation"
        ...
        >>> engine = PythoniteEngine()
        >>> engine.register_representation(MyRepresentation)
        >>> engine.get_representation("my_representation")
        <class '__main__.MyRepresentation'>
        """
        try:
            return self.representations[pythonite_id]
        except KeyError:
            raise RepresentationNotFoundError(
                f"Representation with id {pythonite_id} not found in Pythonite engine."
            )

    def register_template(self, template: "PythoniteTemplate") -> None:
        """
        Register a template with the Pythonite engine. This makes it retrievable from a PythoniteTemplate.

        Args:
            template (PythoniteTemplate): The template to register.
        """
        self.templates[template.template_id] = template

    def get_template(self, template_id: str) -> "PythoniteTemplate":
        """
        Get a template from the Pythonite engine.

        Args:
            template_id (str): The id of the template to get.

        Returns:
            PythoniteTemplate: The template with the given id.

        Example:
        >>> from pythonite_engine import PythoniteEngine
        >>> from pythonite_engine import PythoniteTemplate
        >>> class MyTemplate(PythoniteTemplate):
        ...     template_id = "my_template"
        ...
        >>> engine = PythoniteEngine()
        >>> engine.register_template(MyTemplate)
        >>> engine.get_template("my_template")
        <class '__main__.MyTemplate'>
        """
        try:
            return self.templates[template_id]
        except KeyError:
            raise TemplateNotFoundError(
                f"Template with id {template_id} not found in Pythonite engine."
            )

    def register_component(self, component: Component) -> None:
        """
        Register a component with the Pythonite engine. This makes it retrievable from a PythoniteTemplate.

        Args:
            component (Component): The component to register.
        """
        self.components[component.component_id] = component

    def get_component(self, component_id: str) -> Component:
        """
        Get a component from the Pythonite engine.

        Args:
            component_id (str): The id of the component to get.

        Returns:
            Component: The component with the given id.

        Example:
        >>> from pythonite_engine import PythoniteEngine
        >>> from pythonite_engine import Component
        >>> class MyComponent(Component):
        ...     component_id = "my_component"
        ...
        >>> engine = PythoniteEngine()
        >>> engine.register_component(MyComponent)
        >>> engine.get_component("my_component")
        <class '__main__.MyComponent'>
        """
        try:
            return self.components[component_id]
        except KeyError:
            raise ComponentNotFoundError(
                f"Component with id {component_id} not found in Pythonite engine."
            )
