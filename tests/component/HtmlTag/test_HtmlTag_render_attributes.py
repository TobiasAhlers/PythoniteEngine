import pytest

from pythonite_engine import *


def test_render_no_attributes():
    tag = HtmlTag(tag_name="div")
    assert tag.render_attributes() == ""


def test_render_attribute_with_string_value():
    tag = HtmlTag(tag_name="div", attributes={"id": "my-div"})
    assert tag.render_attributes() == ' id="my-div"'


def test_render_attribute_with_boolean_value():
    tag = HtmlTag(tag_name="div", attributes={"hidden": True})
    assert tag.render_attributes() == " hidden"


def test_render_attribute_with_multiple_values():
    tag = HtmlTag(tag_name="div", attributes={"id": "my-div", "hidden": True})
    assert tag.render_attributes() == ' id="my-div" hidden'
