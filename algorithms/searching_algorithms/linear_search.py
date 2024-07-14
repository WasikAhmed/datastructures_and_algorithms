def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == '__main__':
    array = [5, 3, 8, 4, 2]
    result = linear_search(array, 8)
    print(result)
