from src.maths_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(2, 3) != 6

def test_sub():
    assert sub(3, 2) == 1
    assert sub(3, 2) != 2
    assert sub(2, 3) == -1