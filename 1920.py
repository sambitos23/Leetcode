def permutation(num: list) -> list:
    ans = []
    for index, value in enumerate(num):
        ans.append(num[num[index]])

    return ans


print(permutation([0, 2, 1, 5, 3, 4]))
