import pytest

from pythonite_engine import *


def test_render_no_classes():
    tag = HtmlTag(tag_name="div")
    assert tag.render_classes() == ""


def test_render_single_class():
    tag = HtmlTag(tag_name="div", classes=["my-class"])
    assert tag.render_classes() == ' class="my-class"'


def test_render_multiple_classes():
    tag = HtmlTag(tag_name="div", classes=["my-class", "my-other-class"])
    assert tag.render_classes() == ' class="my-class my-other-class"'
