import pytest
from Program import Sort

def test_string():
    assert Sort.words("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"