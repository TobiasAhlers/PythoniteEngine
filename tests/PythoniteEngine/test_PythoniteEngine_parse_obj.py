import pytest

from pythonite_engine import *


def test_parse_nested_pythonite_representation():
    assert PythoniteEngine().parse_obj(
        {
            "__pythonite_signature__": "StaticValue",
            "value": "Hello, ",
            "type": {"__pythonite_signature__": "StringType"},
        }
    ) == StaticValue(value="Hello, ", type=StringTypeRepresentation())


def test_parse_pythonite_representation():
    assert (
        PythoniteEngine().parse_obj(
            {
                "__pythonite_signature__": "IntegerType",
            }
        )
        == IntegerTypeRepresentation()
    )


def test_parse_dict_of_objs():
    assert PythoniteEngine().parse_obj(
        {
            "arg1": 1,
            "arg2": "Hello, World!",
            "arg3": {
                "__pythonite_signature__": "IntegerType",
            },
            "arg4": {"2": "test"},
            "arg5": [1, 2],
            "arg6": [
                {
                    "__pythonite_signature__": "IntegerType",
                },
                {
                    "__pythonite_signature__": "StringType",
                },
            ],
        }
    ) == {
        "arg1": 1,
        "arg2": "Hello, World!",
        "arg3": IntegerTypeRepresentation(),
        "arg4": {"2": "test"},
        "arg5": [1, 2],
        "arg6": [
            IntegerTypeRepresentation(),
            StringTypeRepresentation(),
        ],
    }


def test_parse_list_of_objs():
    assert PythoniteEngine().parse_obj(
        [
            {
                "__pythonite_signature__": "IntegerType",
            },
            {
                "__pythonite_signature__": "StringType",
            },
        ]
    ) == [IntegerTypeRepresentation(), StringTypeRepresentation()]


def test_parse_list_of_mixed_objs():
    assert PythoniteEngine().parse_obj(
        [
            {
                "__pythonite_signature__": "IntegerType",
            },
            "Hello, World!",
        ]
    ) == [IntegerTypeRepresentation(), "Hello, World!"]


def test_parse_nested_list_of_objs():
    assert PythoniteEngine().parse_obj(
        [
            [
                {
                    "__pythonite_signature__": "IntegerType",
                },
                {
                    "__pythonite_signature__": "StringType",
                },
            ],
            [
                {
                    "__pythonite_signature__": "StringType",
                },
                {
                    "__pythonite_signature__": "IntegerType",
                },
            ],
        ]
    ) == [
        [IntegerTypeRepresentation(), StringTypeRepresentation()],
        [StringTypeRepresentation(), IntegerTypeRepresentation()],
    ]
