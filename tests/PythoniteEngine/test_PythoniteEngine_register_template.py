import pytest

from pythonite_engine import *


def test_register_non_existing():
    engine = PythoniteEngine()
    template = PythoniteTemplate(template_id="my_template")
    engine.register_template(template)

    assert engine.templates["my_template"] == template


def test_register_existing():
    engine = PythoniteEngine()
    template = PythoniteTemplate(template_id="my_template")
    engine.register_template(template)

    template2 = PythoniteTemplate(template_id="my_template", extends="my_template")
    engine.register_template(template2)
    assert engine.templates["my_template"] == template2
