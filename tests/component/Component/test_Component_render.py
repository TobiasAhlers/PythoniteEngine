import pytest

from pythonite_engine import *


def test_render_no_args():
    component = Component(
        component_id="my_component",
        content=[StaticValue(value="Hello, world!", type=StringTypeRepresentation())],
    )
    assert component.render(scope=Scope()) == "Hello, world!"


def test_render_with_args():
    component = Component(
        component_id="my_component",
        annotation={"name": Annotation(type=StringTypeRepresentation(), required=True)},
        content=[
            VariableRetrieval(variable_name="name", type=StringTypeRepresentation())
        ],
    )
    assert component.render(name="Hello, world!", scope=Scope()) == "Hello, world!"


def test_render_with_invalid_args():
    component = Component(
        component_id="my_component",
        jinja2_template="{{ name }}",
        annotation={
            "name": Annotation(type=IntegerTypeRepresentation(), required=True)
        },
    )
    with pytest.raises(ConversionError):
        component.render(name="INVALID", scope=Scope())
