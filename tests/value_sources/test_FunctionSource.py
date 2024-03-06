import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert FunctionSource.__pythonite_signature__ == "FunctionSource"


def test_execute():
    engine = PythoniteEngine()

    def my_function(arg1: int) -> int:
        return arg1 * 2

    engine.register_function(function_id="my_function", function=my_function)

    function_source = FunctionSource(function_id="my_function", args={"arg1": 5})

    assert function_source.execute(scope=Scope(), engine=engine) == 10

    with pytest.raises(FunctionNotFoundError):
        FunctionSource(function_id="my_function_not_found", args={}).execute(
            scope=Scope(), engine=engine
        )

    assert (
        FunctionSource(
            function_id="my_function",
            args={"arg1": StaticValue(value=5, type=IntegerTypeRepresentation())},
        ).execute(scope=Scope(), engine=engine)
        == 10
    )
