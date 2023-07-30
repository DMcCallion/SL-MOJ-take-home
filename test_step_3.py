import pytest

from test_3 import sum_current_time


def test_good_time():  # I'm having a good time!
    assert sum_current_time("11:12:13") == 36


def test_good_time_2():
    assert sum_current_time("04:05:06") == 15


def test_wrong_type_input():
    with pytest.raises(TypeError) as excinfo:
        sum_current_time(1000)
    assert "input must be a string" in str(excinfo.value)


def test_wrong_separator():
    with pytest.raises(ValueError) as excinfo:
        sum_current_time("10-12-55")
    assert "Wrong / No separator used" in str(excinfo.value)


def test_bad_time():  # Hopefully the reader isn't having a bad time!
    with pytest.raises(ValueError) as excinfo:
        sum_current_time("55:99:00")
    assert "Sum too large - Invalid Time" in str(excinfo.value)


def test_negative_number():
    with pytest.raises(ValueError) as excinfo:
        sum_current_time("-12:00:00")
    assert "Sum was negative - Invalid Time" in str(excinfo.value)
