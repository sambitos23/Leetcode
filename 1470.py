def suffel(nums: list, n: int) -> list:
    split_array_first = nums[:n]
    split_array_second = nums[n:]
    ans = []

    for i in range(n):
        ans.append(split_array_first[i])
        ans.append(split_array_second[i])

    return ans


print(suffel([2, 5, 1, 3, 4, 7], 3))
