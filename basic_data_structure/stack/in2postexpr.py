import string

from stack import Stack


def in2postexpr(inexpr: str):
    priority = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opsstack = Stack()
    tokenlist = inexpr.split()
    postexpr = []

    for i in tokenlist:
        if i in string.ascii_uppercase:
            postexpr.append(i)
        elif i == "(":
            opsstack.push(i)
        elif i == ")":
            poptoken = opsstack.pop()
            while poptoken != "(":
                postexpr.append(poptoken)
                poptoken = opsstack.pop()
        else:
            while (not opsstack.isEmpty()) and (
                priority[opsstack.peek()] >= priority[i]
            ):
                postexpr.append(opsstack.pop())
            opsstack.push(i)
    while not opsstack.isEmpty():
        postexpr.append(opsstack.pop())
    return " ".join(postexpr)


def test():
    assert in2postexpr("( A + B ) * ( C + D )") == "A B + C D + *"
    assert in2postexpr("( A + B ) * C") == "A B + C *"


# if __name__ == "__main__":
#     test()
#     print("All test done!")
