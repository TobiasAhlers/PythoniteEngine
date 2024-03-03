import pytest


from pythonite_engine import *


def test_execute():
    identity = IdentityOperatorRepresentation(operator="is", operands=[1, 2])
    assert identity.execute() == False

    identity = IdentityOperatorRepresentation(operator="is not", operands=[1, 2])
    assert identity.execute() == True
