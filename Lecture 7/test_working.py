from working import convert
import pytest

def test_optional_colon():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_12():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_time_to():
    with pytest.raises(ValueError):
        convert("9:70 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("13 AM - 17 PM")