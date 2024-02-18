from typing import Self

from .scope import Scope
from .pythonite_engine import PythoniteEngine
from .pythonite_representation import PythoniteRepresentation


class PythoniteTemplate:
    """
    Represents a Pythonite script.

    If a custom script execution is required, the subclass should override the `execute` method.

    Attributes:
        script (list[PythoniteRepresentation]): The script represented by this class.
        engine (PythoniteEngine): The engine used to execute the script.
        global_scope (Scope): The global scope used for the script.
    """

    def __init__(
        self,
        script: list[PythoniteRepresentation],
        engine: PythoniteEngine,
        global_scope: Scope,
        *args,
        **kwargs
    ) -> None:
        self.script = script
        self.engine = engine
        self.global_scope = global_scope

    @classmethod
    def from_json(
        cls, script: str, engine: PythoniteEngine, global_scope: Scope
    ) -> Self:
        """
        Create a PythoniteTemplate from a JSON string.

        Args:
            script (str): The JSON string representing the script.
            engine (PythoniteEngine): The engine used to execute the script.
            global_scope (Scope): The global scope used for the script.

        Returns:
            PythoniteTemplate: The PythoniteTemplate created from the JSON string.
        """
        raise NotImplementedError()

    def to_json(self) -> str:
        """
        Convert the PythoniteTemplate to a JSON string.

        Returns:
            str: The JSON string representing the PythoniteTemplate.
        """
        raise NotImplementedError()

    def render(self, *args, **kwargs) -> str:
        """
        Render the PythoniteTemplate.

        Args:
            *args: Additional arguments to pass to the rendering.
            **kwargs: Additional keyword arguments to pass to the rendering.

        Returns:
            str: The rendered PythoniteTemplate.
        """
        raise NotImplementedError()