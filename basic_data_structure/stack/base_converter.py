from stack import Stack


def dec2bi(decNum: int) -> str:
    if decNum == 0:
        return "0"

    rem_stack = Stack()

    while decNum > 0:
        rem = decNum % 2
        rem_stack.push(rem)
        decNum = decNum // 2

    bi_str: str = ""
    while not rem_stack.isEmpty():
        bi_str += str(rem_stack.pop())
    return bi_str


def dec2any(decNum: int, base: int) -> str:
    num_str = "0123456789ABCDEF"
    assert (base <= 16) and (base > 0), "最多支持16进制的转化"
    if decNum == 0:
        return "0"

    rem_stack = Stack()
    while decNum > 0:
        rem = decNum % base
        rem_stack.push(rem)
        decNum //= base
    target_str = ""
    while not rem_stack.isEmpty():
        num = num_str[rem_stack.pop()]
        target_str += num
    return target_str


# def test4dec2bi():
#     assert dec2bi(0) == "0"
#     assert dec2bi(1) == "1"
#     assert dec2bi(2) == "10"
#     assert dec2bi(3) == "11"
#     assert dec2bi(8) == "1000"
#     assert dec2bi(255) == "11111111"


# def test4dec2any():
#     assert dec2any(0, 2) == "0"
#     assert dec2any(10, 2) == "1010"
#     assert dec2any(255, 2) == "11111111"
#     assert dec2any(255, 8) == "377"
#     assert dec2any(255, 10) == "255"
#     assert dec2any(255, 16) == "FF"
#     assert dec2any(1234, 16) == "4D2"
#     assert dec2any(1234, 8) == "2322"


# if __name__ == "__main__":
#     test4dec2bi()
#     test4dec2any()
#     print("All test done!")
