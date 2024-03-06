import pytest

from pythonite_engine import *


def test_register_unexisting():
    engine = PythoniteEngine()
    component = Component(component_id="my_component", jinja2_template="")
    engine.register_component(component)

    assert engine.components["my_component"] == component


def test_register_existing():
    engine = PythoniteEngine()
    component = Component(component_id="my_component", jinja2_template="")
    engine.register_component(component)

    component2 = Component(component_id="my_component", jinja2_template="")

    engine.register_component(component2)
    assert engine.components["my_component"] == component2
