import pytest
from source.calculator import add

def test_add():
    assert add("1,2") == 3
    assert add("4,4") == 8
    assert add("8,10") == 18
    assert add("15,15") == 30

