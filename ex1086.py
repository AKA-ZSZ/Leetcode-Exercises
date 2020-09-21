# id=items[i][0], grade=items[i][1]
# get average of top 5 grade of each student
def highFive(items):

    result = []
    temp_dict = {}

    for item in items:
        key = item[0]
        # key not existed
        if key not in temp_dict.keys():
            temp_dict[key] = [[item[1]], item[1]]
        else:
            top_grades = temp_dict[key][0]
            # key existed
            if len(top_grades) <= 5:
                top_grades.append(item[1])

            if temp_dict[key][1] > item[1]:
                temp_dict[key][1] = item[1]
            else:
                if len(top_grades) > 5:
                    top_grades.remove(temp_dict[key][1])
                    top_grades.sort()
                    temp_dict[key][1] = top_grades[0]

    for key, value in temp_dict.items():
        # get average
        avg = sum(value[0]) // len(value[0])
        result.append([key, avg])

    result.sort()
    return result


# testcases
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(highFive(items))
