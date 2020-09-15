# Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
# Return 0 if S is odd, otherwise return 1.
from math import floor


def sumOfDigits(A):
    minNum = min(A)
    S = 0
    while minNum > 0:
        S += minNum % 10
        minNum = floor(minNum / 10)

    result = 1 if S % 2 == 0 else 0
    return result

# testcases
# A = [99, 77, 33, 66, 55]
# A = [34, 23, 1, 24, 75, 33, 54, 8]
# print(sumOfDigits(A))
