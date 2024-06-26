# test_math_operations.py

import pytest
from math_operations import add, sub, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_sub():
    assert sub(2, 1) == 1
    assert sub(-1, -1) == 0
    assert sub(-1, 1) == -2

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
