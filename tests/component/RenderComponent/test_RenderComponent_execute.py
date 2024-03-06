import pytest

from pythonite_engine import *


def test_execute_existing():
    engine = PythoniteEngine()
    component = Component(
        component_id="my_component",
        jinja2_template="Hello, world!",
    )
    engine.register_component(component)

    assert (
        RenderComponent(component_id="my_component").execute(
            scope=Scope(), engine=engine
        )
        == "Hello, world!"
    )


def test_execute_non_existing():
    engine = PythoniteEngine()

    with pytest.raises(ComponentNotFoundError):
        RenderComponent(component_id="my_component").execute(
            scope=Scope(), engine=engine
        )
