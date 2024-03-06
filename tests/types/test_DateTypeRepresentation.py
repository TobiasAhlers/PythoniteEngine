import pytest

from datetime import date

from pythonite_engine import *


def test_pythonite_signature():
    assert DateTypeRepresentation.__pythonite_signature__ == "DateType"


def test_convert_value():
    date_type = DateTypeRepresentation()
    assert date_type.convert_value("2021-01-01") == date(2021, 1, 1)
    
    with pytest.raises(ConversionError) as e:
        date_type.convert_value("2021-01-32")


def test_get_type():
    assert DateTypeRepresentation().get_type() == date


def test_execute():
    date_type = DateTypeRepresentation()
    assert date_type.execute("2021-01-01", Scope()) == date(2021, 1, 1)
    
    with pytest.raises(ConversionError) as e:
        date_type.execute("2021-01-32", Scope())