import pytest

from pythonite_engine import *


def test_execute_with_variable():
    engine = PythoniteEngine()
    engine.register_template(
        template=PythoniteTemplate(
            template_id="test_template",
            content=[
                StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                VariableRetrieval(variable_name="name"),
                StaticValue(value="!", type=StringTypeRepresentation()),
            ],
        )
    )
    scope = Scope()
    scope.declare_variable(variable_name="name", type=StringTypeRepresentation())
    scope.set_variable_value(variable_name="name", value="World")

    assert (
        RenderTemplate(template_id="test_template").execute(scope=scope, engine=engine)
        == "Hello, World!"
    )


def test_execute_without_variable():
    engine = PythoniteEngine()
    engine.register_template(
        template=PythoniteTemplate(
            template_id="test_template",
            content=[
                StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                VariableRetrieval(variable_name="name"),
                StaticValue(value="!", type=StringTypeRepresentation()),
            ],
        )
    )
    scope = Scope()

    with pytest.raises(VariableNotFoundError):
        RenderTemplate(template_id="test_template").execute(scope=scope, engine=engine)
