class Stack:

    def __init__(self) -> None:
        self.__storage = []

    def __len__(self) -> int:
        return len(self.__storage)

    def push(self, item) -> None:
        self.__storage.append(item)

    def pop(self):
        try:
            return self.__storage.pop()
        except IndexError:
            raise IndexError('pop from empty stack')

    def peek(self):
        if len(self.__storage) == 0:
            return None
        else:
            return self.__storage[-1]

    def is_empty(self):
        if len(self.__storage) == 0:
            return True
        else:
            return False