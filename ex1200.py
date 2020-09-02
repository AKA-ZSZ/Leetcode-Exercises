def minimumAbsDifference(arr):
    # sort the arr
    arr.sort()

    olddiff = arr[1] - arr[0]
    result = []

    for i in range(len(arr) - 1):

        newdiff = arr[i + 1] - arr[i]
        temp = [arr[i], arr[i + 1]]
        if newdiff < olddiff:
            olddiff = newdiff
            result = [temp]
        if newdiff == olddiff:
            if temp not in result:
                result.append(temp)

    return result

# testcase
# arr1 = [40, 11, 26, 27, -20]
# print(minimumAbsDifference(arr1))
