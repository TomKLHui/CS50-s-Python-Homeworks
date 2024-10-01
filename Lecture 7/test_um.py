from um import count

def test_multi():
    assert count("Um um. um?") == 3

def test_word_um():
    assert count("Umbral bacterium umbrella?") == 0

