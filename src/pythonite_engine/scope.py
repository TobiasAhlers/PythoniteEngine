from typing import Self, Any, TYPE_CHECKING, Literal

from .errors import (
    VariableAlreadyDeclaredError,
    VariableNotFoundError,
    VariableDeclaredButNotInitializedError,
    VariableError,
)

if TYPE_CHECKING:
    from .types.base import TypeRepresentation


class Scope:
    """
    A class used to represent a Scope.

    Attributes
    ----------
    parent : Scope
        a reference to the parent scope
    variables : dict
        a dictionary to store variable declarations
    """

    def __init__(self, parent: Self = None) -> None:
        self.parent = parent
        self.variables = {}

    def declare_variable(
        self,
        variable_name: str,
        type: "TypeRepresentation",
        scope: Literal["global", "local"] = "local",
    ) -> None:
        """
        Declares a new variable in the current scope.

        Parameters
        ----------
        variable : VariableDeclaration
            The variable to be declared.

        Raises
        ------
        VariableAlreadyDeclaredError
            If the variable is already declared in the current scope.
        """
        if scope == "global" and self.parent is not None:
            return self.parent.declare_variable(
                variable_name=variable_name, type=type, scope=scope
            )
        if variable_name in self.variables:
            raise VariableAlreadyDeclaredError(
                f"The variable '{variable_name}' has already been declared."
            )
        self.variables[variable_name] = {"type": type}

    def get_variable_value(self, variable_name: str) -> Any:
        """
        Returns the value of a variable in the current scope.

        Parameters
        ----------
        variable_name : str
            The name of the variable.

        Raises
        ------
        VariableNotFoundError
            If the variable could not be found in the current scope.
        VariableDeclaredButNotInitializedError
            If the variable is declared but not initialized.
        """
        if variable_name in self.variables:
            try:
                return self.variables[variable_name]["value"]
            except KeyError:
                raise VariableDeclaredButNotInitializedError(
                    f"The variable '{variable_name}' is declared but not initialized."
                )
        if self.parent is not None:
            return self.parent.get_variable_value(variable_name)
        raise VariableNotFoundError(
            f"The variable '{variable_name}' could not be found."
        )

    def set_variable_value(self, variable_name: str, value: Any) -> None:
        """
        Sets the value of a variable in the current scope.

        Parameters
        ----------
        variable_name : str
            The name of the variable.
        value : Any
            The value to be set.

        Raises
        ------
        VariableNotFoundError
            If the variable could not be found in the current scope.
        VariableError
            If the type of the variable could not be retrieved.
        """
        if variable_name in self.variables:
            try:
                self.variables[variable_name]["value"] = self.variables[variable_name][
                    "type"
                ].convert_value(value)
                return
            except KeyError:
                raise VariableError(
                    f"Unable to retrieve the type of the variable '{variable_name}'. This is a bug. Please report it. Thank you. :)\ndebug-info: self.variables[variable_name]: {self.variables[variable_name]}"
                )
        if self.parent is not None:
            self.parent.set_variable_value(variable_name, value)
            return
        raise VariableNotFoundError(
            f"The variable '{variable_name}' could not be found."
        )
