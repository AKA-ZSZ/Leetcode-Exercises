def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    leftParas = ["(", "[", "{"]
    rightParas = [")", "]", "}"]

    # method 1 - brute force

    # if string is empty:valid
    # if s == "":
    #     return True
    # elif s[0] in rightParas:
    #     return False
    # else:
    # lastParas = s[0]
    #
    # for para in s[1::]:
    #     if para in leftParas:
    #         lastParas += para
    #     else:
    #         if lastParas == "":
    #             return False
    #         if leftParas.index(lastParas[-1]) != rightParas.index(para):
    #             return False
    #         else:
    #             lastParas = lastParas[0:len(lastParas) - 1]
    # if lastParas != "":
    #     return False
    #
    # return True

    # method 2 - use stack
    stack = []
    for para in s[0::]:
        if para in leftParas:
            stack.append(rightParas[leftParas.index(para)])
        else:
            if len(stack) == 0 or stack.pop() != para:
                return False
    return len(stack) == 0

# testcases
# s = ""
# s = "()[]{}"
# s = "[([]])"

# print(isValid(s))
