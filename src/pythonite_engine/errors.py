class PythoniteEngineError(Exception):
    """
    The base class for all Pythonite Engine exceptions.
    """


class ConversionError(Exception):
    """
    Raised when a type could not be converted.
    """


class VariableError(PythoniteEngineError):
    """
    The base class for all variable related exceptions.
    """


class VariableAlreadyDeclaredError(VariableError):
    """
    Raised when a variable is declared more than once.
    """


class VariableNotFoundError(VariableError):
    """
    Raised when a variable is not found.
    """


class VariableDeclaredButNotInitializedError(VariableError):
    """
    Raised when a variable is declared but not initialized.
    """


class FunctionError(PythoniteEngineError):
    """
    The base class for all function related exceptions.
    """


class FunctionNotFoundError(FunctionError):
    """
    Raised when a function is not found.
    """


class InvalidFunctionArgumentsError(FunctionError):
    """
    Raised when the arguments passed to a function are invalid.
    """


class InvalidObjectTypeRepresentationError(PythoniteEngineError):
    """
    Raised when a ObjectTypeRepresentation has been wrongly defined.
    """


class NotExecutableError(PythoniteEngineError):
    """
    Raised when an object is not executable.
    """


class FunctionAlreadyRegisteredError(PythoniteEngineError):
    """
    Raised when a function is already registered.
    """


class RepresentationAlreadyRegisteredError(PythoniteEngineError):
    """
    Raised when a representation is already registered.
    """


class RepresentationNotFoundError(PythoniteEngineError):
    """
    Raised when a representation is not found.
    """