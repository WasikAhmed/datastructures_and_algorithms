def counting_sort(arr: list[int]) -> list[int]:
    max_element = max(arr)

    count_arr = [0] * (max_element + 1)
    for num in arr:
        count_arr[num] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    output_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1

    return output_arr


if __name__ == '__main__':
    arr = [2, 9, 10, 1, 2, 5, 2, 6]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)
