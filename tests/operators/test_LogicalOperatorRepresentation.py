import pytest


from pythonite_engine import *


def test_execute():
    logical = LogicalOperatorRepresentation(operator="and", operands=[True, False])
    assert logical.execute() == False

    logical = LogicalOperatorRepresentation(operator="or", operands=[True, False])
    assert logical.execute() == True
