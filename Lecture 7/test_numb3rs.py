from numb3rs import validate

def test_0_256():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("192.512.512.512") ==False
    assert validate("1.2.3.1000") == False
    assert validate("0.0.0.0") == True
def test_dots():
    assert validate("cat") ==False
    assert validate("512.512.512") ==False

