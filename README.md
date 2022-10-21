# Stack

A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This ordering principle is called LIFO, last-in first-out.
The stack operations are given below.

- Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
- push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
- pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
- peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
- is_empty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
- len() returns the number of items on the stack.
  
### Implementing a Stack in Python 

- stack.py