from stack import Stack


def matches(open: str, close: str) -> bool:
    """
    判断不同类型括号左右是否匹配
    """
    opens = "({["
    closes = ")}]"

    return opens.index(open) == closes.index(close)


def parCherker(symbolstring: str) -> bool:
    """
    @symbolstring: str，包含(), {}, []

    @return: bool, 如果对于括号可以正确的两两配对，则返回True
    """
    s = Stack()
    balence = True
    index = 0
    if len(symbolstring) == 0:
        return False
    while index < len(symbolstring) and balence:
        symbol = symbolstring[index]

        if symbol in "({[":
            s.push(symbol)

        else:
            if s.isEmpty():
                balence = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balence = False

        index += 1

    if balence and s.isEmpty():
        return True
    else:
        return False


# def test():
#     assert parCherker("(((((((((())))))))))")
#     assert not parCherker("")
#     assert not parCherker("((())))")
#     assert not parCherker("[)")
#     assert parCherker("[[[[[[[]]]]]]]")
#     assert not parCherker("[][][][[]]]")
#     assert not parCherker("\\{\\{{\\{{\\}}}}")


# if __name__ == "__main__":
#     test()
#     print("All test passed!")
