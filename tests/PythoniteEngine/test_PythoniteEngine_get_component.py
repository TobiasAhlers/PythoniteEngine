import pytest

from pythonite_engine import *


def test_get_existing():
    engine = PythoniteEngine()
    component = Component(component_id="my_component", jinja2_template="")
    engine.components[component.component_id] = component

    assert engine.get_component("my_component") == component


def test_get_non_existing():
    engine = PythoniteEngine()

    with pytest.raises(ComponentNotFoundError):
        engine.get_component("my_component")
