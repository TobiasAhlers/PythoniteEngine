import pytest


from pythonite_engine import *


def test_execute():
    comparison = ComparisonOperatorRepresentation(operator="==", operands=[1, 2])
    assert comparison.execute() == False

    comparison = ComparisonOperatorRepresentation(operator="!=", operands=[1, 2])
    assert comparison.execute() == True

    comparison = ComparisonOperatorRepresentation(operator="<", operands=[1, 2])
    assert comparison.execute() == True

    comparison = ComparisonOperatorRepresentation(operator="<=", operands=[1, 2])
    assert comparison.execute() == True

    comparison = ComparisonOperatorRepresentation(operator=">", operands=[1, 2])
    assert comparison.execute() == False

    comparison = ComparisonOperatorRepresentation(operator=">=", operands=[1, 2])
    assert comparison.execute() == False
