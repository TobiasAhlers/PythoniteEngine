import pytest

from pythonite_engine import *


def test_render_no_args():
    component = Component(
        component_id="my_component",
        jinja2_template="Hello, world!",
    )
    assert component.render() == "Hello, world!"


def test_render_with_args():
    component = Component(
        component_id="my_component",
        jinja2_template="{{ name }}",
        annotation={"name": Annotation(type=StringTypeRepresentation(), required=True)},
    )
    assert component.render(name="Hello, world!") == "Hello, world!"


def test_render_with_invalid_args():
    component = Component(
        component_id="my_component",
        jinja2_template="{{ name }}",
        annotation={"name": Annotation(type=IntegerTypeRepresentation(), required=True)},
    )
    with pytest.raises(ConversionError):
        component.render(name="INVALID")