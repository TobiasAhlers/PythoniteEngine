import pytest

from json import dumps

from pythonite_engine import *


def test_dumps():
    assert PythoniteTemplate(
        template_id="test_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            StaticValue(value="!", type=StringTypeRepresentation()),
        ],
    ).model_dump_json() == dumps(
        {
            "template_id": "test_template",
            "extends": None,
            "content": [
                {
                    "type": {"__pythonite_signature__": "StringType"},
                    "value": "Hello, ",
                    "__pythonite_signature__": "StaticValue",
                },
                {
                    "type": {"__pythonite_signature__": "StringType"},
                    "value": "!",
                    "__pythonite_signature__": "StaticValue",
                },
            ],
        }
    )
