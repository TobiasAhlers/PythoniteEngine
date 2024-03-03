import pytest

from pythonite_engine import *


def test_int():
    assert (
        Annotation(
            type=IntegerTypeRepresentation(), default=10, required=True
        ).validate_annotation(0)
        == 0
    )


def test_float():
    assert (
        Annotation(
            type=FloatTypeRepresentation(), default=10.0, required=True
        ).validate_annotation(0.0)
        == 0.0
    )


def test_str():
    assert (
        Annotation(
            type=StringTypeRepresentation(), default="hello", required=True
        ).validate_annotation("world")
        == "world"
    )


def test_no_default():
    assert (
        Annotation(type=IntegerTypeRepresentation(), required=True).validate_annotation(
            0
        )
        == 0
    )


def test_required():
    with pytest.raises(ConversionError):
        Annotation(type=IntegerTypeRepresentation(), required=True).validate_annotation(
            None
        )


def test_optional():
    assert (
        Annotation(
            type=IntegerTypeRepresentation(), required=False
        ).validate_annotation(None)
        == None
    )


def test_optional_with_default():
    assert (
        Annotation(
            type=IntegerTypeRepresentation(), default=10, required=False
        ).validate_annotation(None)
        == 10
    )