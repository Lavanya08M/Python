from fuel import convert, gauge
import pytest

def test_convert_valid_input():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1/two")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
