# The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
# Given a positive integer N, return true if and only if it is an Armstrong number.

from math import floor, log


def isArmstrong(N):
    # k = digits
    # N=d1**k+d2**k+....+dn**k
    k = floor(log(N, 10)) + 1
    tempN = N
    sum_product = 0
    for i in range(k):
        sum_product += (tempN % 10) ** k
        tempN = floor(tempN / 10)

    return sum_product == N

# testcase
# print(isArmstrong(153))
# print(isArmstrong(123))
