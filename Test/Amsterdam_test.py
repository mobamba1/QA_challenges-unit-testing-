import pytest
from Program import Amsterdam

def test_string():
    assert Amsterdam.ams("Am I in Amsterdam") == 1

def test_string1():
    assert Amsterdam.ams("I am in Amsterdam am I?") == 3

def test_string2():
    assert Amsterdam.ams("I have been in Amsterdam") == 0