import pytest

from pythonite_engine import *


def test_render_with_children():
    scope = Scope()
    scope.declare_variable(variable_name="name", type=StringTypeRepresentation())
    scope.set_variable_value(variable_name="name", value="World")
    assert (
        TemplateChildren().render(
            scope=scope,
            children=[
                StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                VariableRetrieval(variable_name="name"),
                StaticValue(value="!", type=StringTypeRepresentation()),
            ],
        )
        == "Hello, World!"
    )


def test_render_without_children():
    assert TemplateChildren().render(scope=Scope(), children=[]) == ""
