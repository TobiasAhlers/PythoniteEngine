from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pythonite_engine import PythoniteEngine


class EngineExtension:
    """
    Represents an extension for the PythoniteEngine. This class should be subclassed to create an extension.
    An EngineExtension should be used to add custom functionality to the PythoniteEngine.

    Attributes:
        engine (PythoniteEngine): The engine used to execute the script.
    """

    def __init__(self, engine: "PythoniteEngine") -> None:
        self.engine = engine
