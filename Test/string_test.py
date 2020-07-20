import pytest
from Program import string

def test_a_string():
    assert type(string.string_gen("hello")) == str

def test_string_length():
    assert len(string.string_gen("hello")) == 5

def test_string_lowercase():
    assert string.string_gen("hello").islower() == True