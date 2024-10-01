from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")
    with pytest.raises(ValueError):
        assert convert("three/four")
        assert convert("1.5/3")
def test_gauge():
    assert gauge(100)=="F"
    assert gauge(99)=="F"
    assert gauge(0)=="E"
    assert gauge(1)=="E"
    assert gauge(50)=="50%"
