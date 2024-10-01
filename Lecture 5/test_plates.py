from plates import is_valid

def test_2letters():
    assert is_valid("50") ==False
    assert is_valid("CS50") ==True
def test_2to6():
    assert is_valid("H")==False
    assert is_valid("OUTATIME")==False
    assert is_valid("CS")==True
    assert is_valid("ECTO88")==True
    assert is_valid("NRVOUS")==True
def test_nopunctuation():
    assert is_valid("PI3.14")==False
    assert is_valid("PI3 14")==False
    assert is_valid("PI3,14")==False
def test_no_letterafternum_or_0afterletter():
    assert is_valid("CS05")==False
    assert is_valid("CS50P2")==False
