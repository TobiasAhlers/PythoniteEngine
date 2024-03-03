import pytest

from datetime import datetime

from pythonite_engine import *


def test_pythonite_signature():
    assert DateTimeTypeRepresentation.__pythonite_signature__ == "DateTimeType"


def test_convert_value():
    datetime_type = DateTimeTypeRepresentation()
    assert datetime_type.convert_value("2021-01-01 12:00:00") == datetime(
        2021, 1, 1, 12, 0, 0
    )

    with pytest.raises(ConversionError) as e:
        datetime_type.convert_value("2021-01-32 12:00:00")


def test_get_type():
    assert DateTimeTypeRepresentation().get_type() == datetime


def test_execute():
    datetime_type = DateTimeTypeRepresentation()
    assert datetime_type.execute("2021-01-01 12:00:00", Scope()) == datetime(
        2021, 1, 1, 12, 0, 0
    )

    with pytest.raises(ConversionError) as e:
        datetime_type.execute("2021-01-32 12:00:00", Scope())
