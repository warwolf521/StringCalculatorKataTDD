import pytest
from source.calculator import add

def test_add_step1():
    assert add("1,2") == 3
    assert add("4,4") == 8
    assert add("8,10") == 18
    assert add("15,15") == 30

def test_add_step2():
    assert add("1,2,3") == 6
    assert add("8,10,12,14") == 44
    assert add("15,15,15,15,20") == 80
    assert add("4,4,4,7,32,73") == 124