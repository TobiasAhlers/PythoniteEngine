from typing import Optional, Self
from pydantic import BaseModel
from json import loads, dumps

from .scope import Scope
from .pythonite_engine import PythoniteEngine
from .pythonite_representation import PythoniteRepresentation


class PythoniteTemplate(BaseModel):
    """
    Represents a Pythonite script.

    If a custom script execution is required, the subclass should override the `execute` method.

    Attributes:
        script (list[PythoniteRepresentation]): The script represented by this class.
        engine (PythoniteEngine): The engine used to execute the script.
        global_scope (Scope): The global scope used for the script.
    """

    template_id: str
    extends: Optional[str] = None
    content: list[PythoniteRepresentation] = []

    @classmethod
    def model_validate_json(cls, json_data: str, engine: PythoniteEngine) -> Self:
        """
        Validate the JSON data and return a PythoniteTemplate instance.

        Args:
            json_data (str): The JSON data to validate.

        Returns:
            PythoniteTemplate: The PythoniteTemplate instance.
        """
        data = loads(json_data)
        return cls.model_validate(obj=engine.parse_obj(data))
    
    def model_dump_json(self) -> str:
        """
        Dump the PythoniteTemplate instance to JSON.

        Returns:
            str: The JSON representation of the PythoniteTemplate instance.
        """
        return dumps(
            {
                "template_id": self.template_id,
                "extends": self.extends,
                "content": [representation.model_dump() for representation in self.content],
            }
        )
    
    def render(
        self,
        global_scope: Scope,
        engine: PythoniteEngine,
        children: list[PythoniteRepresentation] = [],
        *args,
        **kwargs
    ) -> str:
        """
        Render the PythoniteTemplate.

        Args:
            *args: Additional arguments to pass to the rendering.
            **kwargs: Additional keyword arguments to pass to the rendering.

        Returns:
            str: The rendered PythoniteTemplate.
        """
        if self.extends:
            parent = engine.get_template(template_id=self.extends)
            return parent.render(
                global_scope=global_scope,
                engine=engine,
                children=self.content + children,
                *args,
                **kwargs
            )

        scope = Scope(parent=global_scope)
        html = ""
        for representation in self.content:
            html += str(
                representation.execute(
                    scope=scope, engine=engine, children=children, *args, **kwargs
                )
            )
        return html
