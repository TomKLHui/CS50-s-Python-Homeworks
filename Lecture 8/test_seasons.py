from seasons import validate
from seasons import convert_minutes
import pytest
from datetime import date

def test_dateformat():
    assert validate("January 1, 1999") ==False
    assert validate("1996-02-30") ==False
    assert validate("1996-13-30") ==False
    assert validate("1996-12-30") ==True

