# run with python3 -m pytest -v
from ds.stack import Stack
import pytest

# fixture
@pytest.fixture
def stack():
    return Stack()

# se tra i parametri metto il nome della funzione fixture
# ho la possibilità di usare il valore di ritorno della funzione
# come fosse una variabile
def test_constructor(stack):
    assert isinstance(stack,Stack)
    assert len(stack) == 0

def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2

def test_pop(stack):
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.pop() == "hello"
    with pytest.raises(IndexError):
        stack.pop()

def test_peek(stack):
    stack.push("hello")
    assert stack.peek() == "hello"
    stack.pop()
    assert stack.peek() == None

def test_is_empty(stack):
    assert stack.is_empty()
    stack.push(10)
    assert not stack.is_empty()