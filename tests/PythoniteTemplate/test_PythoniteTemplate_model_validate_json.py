import pytest

from pythonite_engine import *


def test_render_json():
    json = """
{
    "template_id": "example_template",
    "content": [
        {
            "__pythonite_signature__": "ArithmeticOperator",
            "operator": "+",
            "operands": [
                {
                    "__pythonite_signature__": "StaticValue",
                    "value": 1,
                    "type": {
                        "__pythonite_signature__": "IntegerType"
                    }
                },
                {
                    "__pythonite_signature__": "FunctionSource",
                    "function_id": "get_current_user_id",
                    "args": {}
                }
            ]
        },
        {
            "__pythonite_signature__": "ForLoop",
            "loop_variable_name": "user",
            "iterable": {
                "__pythonite_signature__": "FunctionSource",
                "function_id": "get_all_users",
                "args": {}
            },
            "loop_variable_annotation": {
                "__pythonite_signature__" : "Annotation",
                "type" : {
                    "__pythonite_signature__" : "DictionaryType"
                }
            },
            "body": [
                {
                    "__pythonite_signature__": "RenderComponent",
                    "component_id": "user_card",
                    "args": {
                        "user_id": {
                            "__pythonite_signature__": "IndexAccessOperator",
                            "index": "id",
                            "operands": {
                                "__pythonite_signature__": "VariableRetrieval",
                                "variable_name": "user"
                            }
                        },
                        "user_name": {
                            "__pythonite_signature__": "IndexAccessOperator",
                            "index": "name",
                            "operands": {
                                "__pythonite_signature__": "VariableRetrieval",
                                "variable_name": "user"
                            }
                        }
                    }
                }
            ]
        }
    ]
}
"""

    def get_current_user_id():
        return 1

    def get_all_users():
        return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

    component = Component(
        component_id="user_card",
        jinja2_template="{{ user_id }}: {{ user_name }}",
        annotation={
            "user_id": Annotation(type=IntegerTypeRepresentation()),
            "user_name": Annotation(type=StringTypeRepresentation()),
        },
    )

    engine = PythoniteEngine()
    engine.register_function(
        function_id="get_current_user_id", function=get_current_user_id
    )
    engine.register_function(function_id="get_all_users", function=get_all_users)
    engine.register_component(component=component)

    template = PythoniteTemplate.model_validate_json(json, engine=engine)
    assert template == PythoniteTemplate(
        template_id="example_template",
        content=[
            ArithmeticOperatorRepresentation(
                operator="+",
                operands=[
                    StaticValue(value=1, type=IntegerTypeRepresentation()),
                    FunctionSource(function_id="get_current_user_id", args={}),
                ],
            ),
            ForLoop(
                loop_variable_name="user",
                iterable=FunctionSource(function_id="get_all_users", args={}),
                loop_variable_annotation=Annotation(
                    type=DictionaryTypeRepresentation()
                ),
                body=[
                    RenderComponent(
                        component_id="user_card",
                        args={
                            "user_id": IndexAccessOperatorRepresentation(
                                index="id",
                                operands=VariableRetrieval(variable_name="user"),
                            ),
                            "user_name": IndexAccessOperatorRepresentation(
                                index="name",
                                operands=VariableRetrieval(variable_name="user"),
                            ),
                        },
                    ),
                ],
            ),
        ],
    )

    assert template.render(global_scope=Scope(), engine=engine) == "21: John2: Jane"