# Given a matrix mat where every row is sorted in increasing order,
# return the smallest common element in all rows.

from math import floor, ceil


def smallestCommonElement(mat):
    for num in mat[0]:
        count = 0
        for i in range(1, len(mat)):
            # if num not in mat[i]:
            if not binarySearch(num, mat[i]):
                break
            count += 1
        if count == len(mat) - 1:
            return num
    return -1


def binarySearch(x, sortedArr):
    low = 0
    high = len(sortedArr) - 1
    if x == sortedArr[low] or x == sortedArr[high]:
        return True
    if x < sortedArr[low] or x > sortedArr[high]:
        return False
    while low <= high:
        # odd
        if (high + 1) % 2 == 1:
            mid = floor((low + high) / 2)
            if x == sortedArr[mid]:
                return True
            if x > sortedArr[mid]:
                low = mid + 1
            if x < sortedArr[mid]:
                high = mid - 1
        # even
        else:
            mid1 = floor((low + high) / 2)
            mid2 = ceil((low + high) / 2)
            if x == sortedArr[mid1] or x == sortedArr[mid2]:
                return True
            if sortedArr[mid1] < x < sortedArr[mid2]:
                return False
            if x > sortedArr[mid2]:
                low = mid2 + 1
            if x < sortedArr[mid1]:
                high = mid1 - 1
    return False

# testcase
# mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11, 12], [1, 3, 5, 7, 9]]
# print(smallestCommonElement(mat))
