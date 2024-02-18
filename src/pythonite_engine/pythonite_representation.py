from pydantic import BaseModel, ConfigDict
from pydantic.json_schema import DEFAULT_REF_TEMPLATE
from typing import Any, ClassVar, Literal
from json import dumps
from pydantic.json_schema import GenerateJsonSchema

from .scope import Scope


class PythoniteRepresentation(BaseModel):
    """
    Represents a Pythonite representation.

    This class is intended to be subclassed to create custom representations for the Pythonite engine.
    The subclass should override the __pythonite_signature__ attribute to provide a signature for the representation
    with which it can be identified.

    Example:
    >>> from pythonite_engine.pythonite_representation import PythoniteRepresentation
    >>> class MyRepresentation(PythoniteRepresentation):
    ...     __pythonite_signature__ = "MyRepresentation"
    ...
    >>> MyRepresentation.__pythonite_signature__
    'MyRepresentation'
    """

    __pythonite_signature__: ClassVar[str]

    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=False)

    def model_dump(
        self,
        *,
        mode: str = "python",
        include: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
        exclude: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> dict[str, Any]:
        """
        Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

        Args:
            mode: The mode in which `to_python` should run.
                If mode is 'json', the output will only contain JSON serializable types.
                If mode is 'python', the output may contain non-JSON-serializable Python objects.
            include: A list of fields to include in the output.
            exclude: A list of fields to exclude from the output.
            by_alias: Whether to use the field's alias in the dictionary key if defined.
            exclude_unset: Whether to exclude fields that have not been explicitly set.
            exclude_defaults: Whether to exclude fields that are set to their default value.
            exclude_none: Whether to exclude fields that have a value of `None`.
            round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
            warnings: Whether to log warnings when invalid fields are encountered.

        Returns:
            A dictionary representation of the model.
        """
        return super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        ) | {"__pythonite_signature__": self.__pythonite_signature__}

    def model_dump_json(
        self,
        *,
        indent: int | None = None,
        include: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
        exclude: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
    ) -> str:
        """
        Generates a JSON representation of the model using Pydantic's `to_json` method.

        Args:
            indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
            include: Field(s) to include in the JSON output.
            exclude: Field(s) to exclude from the JSON output.
            by_alias: Whether to serialize using field aliases.
            exclude_unset: Whether to exclude fields that have not been explicitly set.
            exclude_defaults: Whether to exclude fields that are set to their default value.
            exclude_none: Whether to exclude fields that have a value of `None`.
            round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
            warnings: Whether to log warnings when invalid fields are encountered.

        Returns:
            A JSON string representation of the model.
        """
        return dumps(
            {"__pythonite_signature__": self.__pythonite_signature__}
            | super().model_dump(
                mode="python",
                include=include,
                exclude=exclude,
                by_alias=by_alias,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
                round_trip=round_trip,
                warnings=warnings,
            ),
            indent=indent,
        )

    @classmethod
    def model_json_schema(
        cls,
        by_alias: bool = True,
        ref_template: str = DEFAULT_REF_TEMPLATE,
        schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
        mode: Literal["validation", "serialization"] = "validation",
    ) -> dict[str, Any]:
        """Generates a JSON schema for a model class.

        Args:
            by_alias: Whether to use attribute aliases or not.
            ref_template: The reference template.
            schema_generator: To override the logic used to generate the JSON schema, as a subclass of
                `GenerateJsonSchema` with your desired modifications
            mode: The mode in which to generate the schema.

        Returns:
            The JSON schema for the given model class.
        """
        return super().model_json_schema(
            by_alias=by_alias,
            ref_template=ref_template,
            schema_generator=schema_generator,
            mode=mode,
        ) | {"__pythonite_signature__": cls.__pythonite_signature__}

    def __str__(self) -> str:
        """
        Returns a string representation of the model.

        Returns:
            str: A string representation of the model.
        """
        return f"__pythonite_signature__='{self.__pythonite_signature__}' {super().__str__()}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the model.

        Returns:
            str: A string representation of the model.
        """
        return f"{self.__class__.__name__}({self.__str__()})"

    def execute(self, scope: Scope, *args, **kwargs) -> Any:
        """
        Execute the action represented by this class.

        Args:
            scope (Scope): The scope to use for the execution.
        """
        raise NotImplementedError(
            f"Expected subclass of PythoniteRepresentation {self.__class__.__name__} to implement execute method."
        )
