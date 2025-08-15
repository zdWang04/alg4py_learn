from stack import Stack


def domath(ops: str, num1: int | float, num2: int | float):
    if ops == "*":
        return num1 * num2
    elif ops == "/":
        return num1 / num2
    elif ops == "+":
        return num1 + num2
    else:
        return num1 - num2


def calculate_postexpr(postexpr: str) -> int | float:
    ops_stack = Stack()
    token_list: list[str] = postexpr.split()

    for i in token_list:
        if i.isdigit():
            ops_stack.push(eval(i))
        else:
            num2 = ops_stack.pop()
            num1 = ops_stack.pop()
            ops_stack.push(domath(i, num1, num2))

    return ops_stack.pop()


# def test():
#     assert calculate_postexpr("2 3 +") == 5
#     assert calculate_postexpr("4 5 *") == 20
#     assert calculate_postexpr("10 2 /") == 5
#     assert calculate_postexpr("8 3 -") == 5
#     assert calculate_postexpr("2 3 + 4 *") == 20  # (2+3)*4
#     assert calculate_postexpr("5 1 2 + 4 * + 3 -") == 14  # 5 + ((1+2)*4) - 3
#     assert calculate_postexpr("7 2 3 * -") == 1  # 7-(2*3)
#     assert calculate_postexpr("3 4 + 2 * 7 /") == 2  # ((3+4)*2)/7
#     print("All tests passed.")


# if __name__ == "__main__":
#     test()
