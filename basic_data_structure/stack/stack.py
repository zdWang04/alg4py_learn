from typing import Any


class Stack:
    def __init__(self):
        self.stack: list[Any] = []

    def isEmpty(self) -> bool:
        return self.stack == []

    def push(self, something: Any) -> None:
        return self.stack.append(something)

    def pop(self) -> Any:
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)

    def peek(self) -> Any:
        return self.stack[self.size() - 1]


# def test1():
#     s = Stack()
#     assert s.isEmpty() is True
#     s.push(1)
#     assert s.isEmpty() is False
#     assert s.pop() == 1
#     assert s.isEmpty() is True


# if __name__ == "__main__":
#     test1()
#     print("Stack test passed.")
