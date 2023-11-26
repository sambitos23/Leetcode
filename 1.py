def two_sum(input_array: list, target: int) -> list:
    num_dict = {}
    for index, value in enumerate(input_array):
        complement = target - value
        if complement in num_dict:
            return [num_dict[complement], index]
        num_dict[value] = index
    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 3], 6))


# using sorting
def two_sum_sort(input_array: list, target: int) -> list:
    sorted_array = sorted(input_array)
    length = len(sorted_array)
    try:
        constant = sorted_array[0]
    except:
        return []

    if constant + sorted_array[length - 1] > target:
        sorted_array = sorted_array[:-1]
        return two_sum_sort(sorted_array, target)
    elif constant + sorted_array[length - 1] < target:
        sorted_array = sorted_array[1:]
        return two_sum_sort(sorted_array, target)
    return [input_array.index(constant), input_array.index(sorted_array[length - 1])]


print(two_sum_sort([2, 7, 11, 15], 9))
print(two_sum_sort([3, 2, 4], 6))
print(two_sum_sort([3, 3], 6))
