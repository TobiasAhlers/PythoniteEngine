from typing import Any

from .pythonite_representation import PythoniteRepresentation


def execute_representations(obj: Any, *args, **kwargs) -> Any:
    """
    Execute the Pythonite representations in the given object.

    Args:
        obj (Any): The object to execute the Pythonite representations in.

    Returns:
        Any: The result of the execution.
    """
    if isinstance(obj, PythoniteRepresentation):
        return obj.execute(*args, **kwargs)
    elif isinstance(obj, list):
        return [execute_representations(item, *args, **kwargs) for item in obj]
    elif isinstance(obj, dict):
        return {key: execute_representations(value, *args, **kwargs) for key, value in obj.items()}
    return obj
