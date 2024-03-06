import pytest

from pythonite_engine import *


def test_get_existing():
    engine = PythoniteEngine()
    engine.templates["my_template"] = PythoniteTemplate(template_id="my_template")

    assert engine.get_template("my_template") == PythoniteTemplate(
        template_id="my_template"
    )


def test_get_non_existing():
    engine = PythoniteEngine()

    with pytest.raises(TemplateNotFoundError):
        engine.get_template("my_template")
