from itertools import accumulate


def decode(encoded: list[int], first: int) -> list[int]:
    return list(accumulate([first] + encoded, lambda x, y: x ^ y))


print(decode([1, 2, 3], 1))
