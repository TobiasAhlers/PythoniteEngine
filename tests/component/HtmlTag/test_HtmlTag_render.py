import pytest

from pythonite_engine import *


def test_render_no_attributes():
    tag = HtmlTag(tag_name="div")
    assert tag.render(Scope()) == "<div></div>"


def test_render_single_attribute():
    tag = HtmlTag(tag_name="div", attributes={"id": "my-div"})
    assert tag.render(Scope()) == '<div id="my-div"></div>'


def test_render_single_style():
    tag = HtmlTag(tag_name="div", styles={"color": "red"})
    assert tag.render(Scope()) == '<div style="color: red"></div>'


def test_render_single_class():
    tag = HtmlTag(tag_name="div", classes=["my-class"])
    assert tag.render(Scope()) == '<div class="my-class"></div>'


def test_render_single_content():
    tag = HtmlTag(
        tag_name="div",
        content=[StaticValue(value="Hello, world!", type=StringTypeRepresentation())],
    )
    assert tag.render(Scope()) == "<div>Hello, world!</div>"


def test_render_multiple_content():
    tag = HtmlTag(
        tag_name="div",
        content=[
            StaticValue(value="Hello, world!", type=StringTypeRepresentation()),
            StaticValue(value="Hello, world!", type=StringTypeRepresentation()),
        ],
    )
    assert tag.render(Scope()) == "<div>Hello, world!Hello, world!</div>"


def test_render_multiple_attributes():
    tag = HtmlTag(tag_name="div", attributes={"id": "my-div", "hidden": True})
    assert tag.render(Scope()) == '<div id="my-div" hidden></div>'
