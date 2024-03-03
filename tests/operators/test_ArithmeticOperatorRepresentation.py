import pytest


from pythonite_engine import *


def test_execute():
    arithmetic = ArithmeticOperatorRepresentation(operator="+", operands=[1, 2])
    assert arithmetic.execute() == 3

    arithmetic = ArithmeticOperatorRepresentation(operator="-", operands=[1, 2])
    assert arithmetic.execute() == -1

    arithmetic = ArithmeticOperatorRepresentation(operator="*", operands=[1, 2])
    assert arithmetic.execute() == 2

    arithmetic = ArithmeticOperatorRepresentation(operator="/", operands=[1, 2])
    assert arithmetic.execute() == 0.5

    arithmetic = ArithmeticOperatorRepresentation(operator="//", operands=[1, 2])
    assert arithmetic.execute() == 0

    arithmetic = ArithmeticOperatorRepresentation(operator="%", operands=[1, 2])
    assert arithmetic.execute() == 1

    arithmetic = ArithmeticOperatorRepresentation(operator="**", operands=[1, 2])
    assert arithmetic.execute() == 1
