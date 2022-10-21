class Stack:

    def __init__(self) -> None:
        self._storage = []

    def __len__(self) -> int:
        return len(self._storage)

    def push(self, item) -> None:
        self._storage.append(item)

    def pop(self):
        try:
            return self._storage.pop()
        except IndexError:
            raise IndexError('pop from empty stack')

    def peek(self):
        if len(self._storage) == 0:
            return None
        else:
            return self._storage[-1]