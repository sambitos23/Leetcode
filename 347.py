num_array = [1, 1, 1, 1, 2, 2, 3, 3, 3, 5, 5, 5, 5]
K = 3


def k_freq_elem(array: list, k: int):
    frequency_array = []
    frequency_dict = {i: array.count(i) for i in array}
    print(frequency_dict)
    sorted_x = sorted(frequency_dict.items(), key=lambda w: w[1], reverse=True)
    print(sorted_x)
    for i in sorted_x:
        frequency_array.append(i[0])

    print(frequency_array[:k])


if __name__ == '__main__':
    k_freq_elem(num_array, K)
