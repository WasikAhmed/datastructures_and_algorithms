def binary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low < high:
        # mid = (low + high) // 2
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 9, 11, 13, 16, 19, 22]

    print(binary_search(nums, 19))
    print(binary_search(nums, 3))
    print(binary_search(nums, 30))
