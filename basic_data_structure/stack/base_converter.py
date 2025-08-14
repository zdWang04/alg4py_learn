from stack import Stack


def dec2bi(decNum: int) -> str:
    if decNum == 0:
        return "0"

    rem_stack = Stack()

    while decNum > 0:
        rem = decNum % 2
        rem_stack.push(rem)
        decNum = decNum // 2

    bi_str = ""
    while not rem_stack.isEmpty():
        bi_str += str(rem_stack.pop())
    return bi_str


# def test():
#     assert dec2bi(0) == "0"
#     assert dec2bi(1) == "1"
#     assert dec2bi(2) == "10"
#     assert dec2bi(3) == "11"
#     assert dec2bi(8) == "1000"
#     assert dec2bi(255) == "11111111"


# if __name__ == "__main__":
#     test()
#     print("All test done!")
