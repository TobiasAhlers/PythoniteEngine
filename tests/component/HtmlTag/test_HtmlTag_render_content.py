import pytest

from pythonite_engine import *


def test_render_no_content():
    tag = HtmlTag(tag_name="div")
    assert tag.render_content(Scope()) == ""


def test_render_single_content():
    tag = HtmlTag(
        tag_name="div",
        content=[StaticValue(value="Hello, world!", type=StringTypeRepresentation())],
    )
    assert tag.render_content(Scope()) == "Hello, world!"


def test_render_multiple_content():
    tag = HtmlTag(
        tag_name="div",
        content=[
            StaticValue(value="Hello, world!", type=StringTypeRepresentation()),
            StaticValue(value="Hello, world!", type=StringTypeRepresentation()),
        ],
    )
    assert tag.render_content(Scope()) == "Hello, world!Hello, world!"
