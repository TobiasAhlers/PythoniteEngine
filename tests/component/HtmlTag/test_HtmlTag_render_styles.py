import pytest

from pythonite_engine import *


def test_render_no_styles():
    tag = HtmlTag(tag_name="div")
    assert tag.render_styles() == ""


def test_render_single_style():
    tag = HtmlTag(tag_name="div", styles={"color": "red"})
    assert tag.render_styles() == ' style="color: red"'


def test_render_multiple_styles():
    tag = HtmlTag(tag_name="div", styles={"color": "red", "font-size": "16px"})
    assert tag.render_styles() == ' style="color: red;font-size: 16px"'
