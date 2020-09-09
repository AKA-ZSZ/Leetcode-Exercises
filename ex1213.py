def arraysIntersection(arr1, arr2, arr3):
    result = []
    for num in arr1:
        if num in arr2 and num in arr3:
            result.append(num)

    return result

# testcases
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [1, 2, 5, 7, 9]
# arr3 = [1, 3, 4, 5, 8]
# print(arraysIntersection(arr1, arr2, arr3))
