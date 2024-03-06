import pytest

from pythonite_engine import *


def test_render_existing():
    engine = PythoniteEngine()
    component = Component(
        component_id="my_component",
        jinja2_template="Hello, world!",
    )
    engine.register_component(component)

    RenderComponent(component_id="my_component").render(
        scope=Scope(), engine=engine
    ) == "Hello, world!"


def test_render_non_existing():
    engine = PythoniteEngine()

    with pytest.raises(ComponentNotFoundError):
        RenderComponent(component_id="my_component").render(
            scope=Scope(), engine=engine
        )
