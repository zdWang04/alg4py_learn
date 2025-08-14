from __future__ import annotations

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

    def reverse(self) -> list[Any]:
        """
        并不会创建一个新的Stack，只是把原来的Stack给反转
        """
        return self.stack[::-1]

    def __repr__(self) -> str:
        rep_list = [str(i) for i in self.stack]
        return f"Stack[{','.join(rep_list)}]"


# def test1():
#     s = Stack()
#     assert s.isEmpty() is True
#     s.push(1)
#     assert s.isEmpty() is False
#     assert s.pop() == 1
#     assert s.isEmpty() is True

#     s.push(1)
#     s.push(2)
#     print(s)
#     assert s.reverse() == [2, 1]
#     print(s)


# if __name__ == "__main__":
#     test1()
#     print("Stack test passed.")
