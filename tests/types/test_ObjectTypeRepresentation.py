import pytest

from pythonite_engine import *


def test_pythonite_signature():
    assert ObjectTypeRepresentation.__pythonite_signature__ == "ObjectType"


def test_convert_value():
    object_type = ObjectTypeRepresentation(
        properties={
            "integer": IntegerTypeRepresentation(),
            "string": StringTypeRepresentation(),
            "boolean": BooleanTypeRepresentation(),
            "float": FloatTypeRepresentation(),
            "default": AnyTypeRepresentation(),
            "required": AnyTypeRepresentation(),
        },
        defaults={"default": 1},
        required=["required"],
    )
    assert object_type.convert_value(
        {"integer": 1, "string": "Hello", "boolean": True, "float": 1.5, "required": 1}
    ) == {
        "integer": 1,
        "string": "Hello",
        "boolean": True,
        "float": 1.5,
        "default": 1,
        "required": 1,
    }

    with pytest.raises(ConversionError) as e:
        object_type.convert_value(
            {"integer": 1, "string": "Hello", "boolean": True, "float": 1.5}
        )


def test_get_type():
    assert ObjectTypeRepresentation().get_type() == dict


def test_execute():
    object_type = ObjectTypeRepresentation(
        properties={
            "integer": IntegerTypeRepresentation(),
            "string": StringTypeRepresentation(),
            "boolean": BooleanTypeRepresentation(),
            "float": FloatTypeRepresentation(),
            "default": AnyTypeRepresentation(),
            "required": AnyTypeRepresentation(),
        },
        defaults={"default": 1},
        required=["required"],
    )
    assert object_type.execute(
        {"integer": 1, "string": "Hello", "boolean": True, "float": 1.5, "required": 1},
        Scope(),
    ) == {
        "integer": 1,
        "string": "Hello",
        "boolean": True,
        "float": 1.5,
        "default": 1,
        "required": 1,
    }

    with pytest.raises(ConversionError) as e:
        object_type.execute(
            {"integer": 1, "string": "Hello", "boolean": True, "float": 1.5}, Scope()
        )
