from twttr import shorten

def test_CS50():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
def test_stress():
    assert shorten("education") == "dctn"
    assert shorten("EVACUATION") == "VCTN"