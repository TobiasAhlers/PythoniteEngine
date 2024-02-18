from typing import Optional, ClassVar

from ..pythonite_representation import PythoniteRepresentation
from ..scope import Scope


class TemplateBlock(PythoniteRepresentation):
    """
    Represents a block in a template in the Pythonite engine.

    Attributes:
        block_id (str): The id of the block represented by this class.
        parent_id (Optional[str]): The id of the parent block of the block represented by this class.
        content (list[PythoniteRepresentation]): The content of the block represented by this class.
    """

    __pythonite_signature__: ClassVar[str] = "TemplateBlock"

    block_id: str
    parent_id: Optional[str]
    content: list[PythoniteRepresentation]

    def render(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the block represented by this class.

        Args:
            scope (Scope): The scope to use as a parent for the rendering.

        Returns:
            str: The rendered block.
        """
        raise NotImplementedError()

    def execute(self, scope: Scope, *args, **kwargs) -> str:
        """
        Render the block represented by this class.

        Args:
            scope (Scope): The scope to use as a parent for the rendering.

        Returns:
            str: The rendered block.
        """
        return self.render(scope=scope, *args, **kwargs)
