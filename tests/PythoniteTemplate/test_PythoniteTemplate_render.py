import pytest

from pythonite_engine import *


def test_not_extends():
    assert (
        PythoniteTemplate(
            template_id="test_template",
            content=[
                StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                StaticValue(value="!", type=StringTypeRepresentation()),
            ],
        ).render(global_scope=Scope(), engine=PythoniteEngine())
        == "Hello, !"
    )


def test_extends():
    parent_template = PythoniteTemplate(
        template_id="parent_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            StaticValue(value="!", type=StringTypeRepresentation()),
            TemplateChildren(),
        ],
    )
    engine = PythoniteEngine()
    engine.register_template(
        template=parent_template,
    )
    child_template = PythoniteTemplate(
        template_id="child_template",
        extends="parent_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            StaticValue(value="!", type=StringTypeRepresentation()),
        ],
    )
    assert (
        child_template.render(global_scope=scope, engine=engine) == "Hello, !Hello, !"
    )


def test_extends_no_TemplateChildren():
    parent_template = PythoniteTemplate(
        template_id="parent_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            StaticValue(value="!", type=StringTypeRepresentation()),
        ],
    )
    engine = PythoniteEngine()
    engine.register_template(
        template=parent_template,
    )
    child_template = PythoniteTemplate(
        template_id="child_template",
        extends="parent_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            StaticValue(value="!", type=StringTypeRepresentation()),
        ],
    )
    assert child_template.render(global_scope=scope, engine=engine) == "Hello, !"


def test_variable_retrieval():
    template = PythoniteTemplate(
        template_id="test_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            VariableRetrieval(variable_name="name"),
            StaticValue(value="!", type=StringTypeRepresentation()),
        ],
    )
    global_scope = Scope()
    global_scope.declare_variable(variable_name="name", type=StringTypeRepresentation())
    global_scope.set_variable_value(variable_name="name", value="World")

    assert (
        template.render(global_scope=global_scope, engine=PythoniteEngine())
        == "Hello, World!"
    )


def test_extends_with_variable_in_both():
    parent_template = PythoniteTemplate(
        template_id="parent_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            VariableRetrieval(variable_name="name"),
            StaticValue(value="!", type=StringTypeRepresentation()),
            TemplateChildren(),
        ],
    )
    engine = PythoniteEngine()
    engine.register_template(
        template=parent_template,
    )
    child_template = PythoniteTemplate(
        template_id="child_template",
        extends="parent_template",
        content=[
            StaticValue(value="Hello, ", type=StringTypeRepresentation()),
            VariableRetrieval(variable_name="name"),
            StaticValue(value="!", type=StringTypeRepresentation()),
        ],
    )
    scope = Scope()
    scope.declare_variable(variable_name="name", type=StringTypeRepresentation())
    scope.set_variable_value(variable_name="name", value="World")

    assert (
        child_template.render(global_scope=scope, engine=engine)
        == "Hello, World!Hello, World!"
    )


def test_function_souce():
    template = PythoniteTemplate(
        template_id="test_template",
        content=[
            FunctionSource(
                function_id="test_function",
                args={"name": "str"},
            ),
        ],
    )

    def test_function(name: str):
        return f"Hello, {name}!"

    engine = PythoniteEngine()
    engine.register_function(function_id="test_function", function=test_function)

    assert template.render(global_scope=Scope(), engine=engine) == "Hello, str!"


def test_function_source_with_variable_retrieval():
    template = PythoniteTemplate(
        template_id="test_template",
        content=[
            FunctionSource(
                function_id="test_function",
                args={"name": VariableRetrieval(variable_name="name")},
            ),
        ],
    )
    global_scope = Scope()
    global_scope.declare_variable(variable_name="name", type=StringTypeRepresentation())
    global_scope.set_variable_value(variable_name="name", value="World")

    def test_function(name: str):
        return f"Hello, {name}!"

    engine = PythoniteEngine()
    engine.register_function(function_id="test_function", function=test_function)

    assert template.render(global_scope=global_scope, engine=engine) == "Hello, World!"


def test_conditional_statement():
    template = PythoniteTemplate(
        template_id="test_template",
        content=[
            ConditionalStatement(
                condition=ComparisonOperatorRepresentation(
                    operator="==",
                    operands=[
                        VariableRetrieval(variable_name="name"),
                        StaticValue(value="World", type=StringTypeRepresentation()),
                    ],
                ),
                consequent=[
                    StaticValue(value="Hello, ", type=StringTypeRepresentation()),
                    VariableRetrieval(variable_name="name"),
                    StaticValue(value="!", type=StringTypeRepresentation()),
                ],
            ),
        ],
    )
    global_scope = Scope()
    global_scope.declare_variable(variable_name="name", type=StringTypeRepresentation())
    global_scope.set_variable_value(variable_name="name", value="World")

    assert (
        template.render(global_scope=global_scope, engine=PythoniteEngine())
        == "Hello, World!"
    )
