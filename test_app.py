from app import add,divide
import pytest
def test_add():
    assert add(1,2) == 3
def test_divide():
    assert divide(2,1) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2,0)
