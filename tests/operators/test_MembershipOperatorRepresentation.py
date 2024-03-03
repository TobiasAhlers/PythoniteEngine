import pytest


from pythonite_engine import *


def test_execute():
    membership = MembershipOperatorRepresentation(operator="in", operands=[1, [1, 2]])
    assert membership.execute() == True

    membership = MembershipOperatorRepresentation(
        operator="not in", operands=[1, [1, 2]]
    )
    assert membership.execute() == False
