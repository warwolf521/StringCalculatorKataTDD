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

def test_add_step3():
    assert add("1\n2") == 3
    assert add("4\n4,4") == 12
    assert add("8,10\n12,14") == 44
    assert add("15\n15,30\n45") == 105

def test_add_step4():
    assert add("//;\n1;2") == 3
    assert add("//;\n4;4;4") == 12
    assert add("//-\n8-10-12-14") == 44
    assert add("//?\n5?9?15?29") == 58

def test_add_step5():
    with pytest.raises(Exception) as excinfo:
        add("-1,2")
    assert str(excinfo.value) == "negatives not allowed: -1"

    with pytest.raises(Exception) as excinfo:
        add("4,-4,4")
    assert str(excinfo.value) == "negatives not allowed: -4"

    with pytest.raises(Exception) as excinfo:
        add("-8,-10,12,-14")
    assert str(excinfo.value) == "negatives not allowed: -8, -10, -14"

    with pytest.raises(Exception) as excinfo:
        add("//;\n-5;-9;15;-29")
    assert str(excinfo.value) == "negatives not allowed: -5, -9, -29"

def test_add_step6():
    assert add("2,1001") == 2
    assert add("1000,1000") == 2000
    assert add("1001,1002") == 0
    assert add("//;\n1001;1002") == 0
    assert add("//-\n1001-1002") == 0
    assert add("//?\3?1002") == 3