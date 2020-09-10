# Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S
# and S < K. If no i, j exist satisfying this equation, return -1.


def twoSumLessThanK(A, K):
    A.sort()

    max_sum = -1
    left = 0
    right = len(A) - 1
    while left < right:
        sum_A = A[left] + A[right]
        if K > sum_A > max_sum:
            max_sum = sum_A
        elif sum_A > K:
            right -= 1
        else:
            left += 1

    return max_sum

# testcase
# A1 = [10, 20, 30]
# K1 = 15
# print(twoSumLessThanK(A1, K1))
