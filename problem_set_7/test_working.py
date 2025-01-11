from working import convert, convert_to_24
import pytest

def test_correct_time_pattern():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_incorrect_time_pattern():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert_to_24():
    assert convert_to_24("AM", "9") == "09:00"
    assert convert_to_24("PM", "5") == "17:00"