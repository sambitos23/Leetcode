def kidsWithCandies(candies: list, extraCandies: int) -> list:
    max_elem = max(candies)
    ans = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_elem:
            ans.append(True)
        else:
            ans.append(False)

    return ans


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
