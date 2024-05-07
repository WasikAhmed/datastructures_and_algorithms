# Binary search is a search algorithm that finds the position of a target value within a sorted array.
# Binary search compares the target value to the middle element of the array.
# If they are not equal, the half in which the target cannot lie is eliminated
# and the search continues on the remaining half.
# again taking the middle element to compare to the target value, and repeating this until the target value is found.
# If the search ends with the remaining half being empty, the target is not in the array.

# The time complexity of Binary Search O(log N).

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
    array_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    result = binary_search(array_1, 3)
    print(result)

    array_2 = [9, 2, 7, 4, 11, 5, 8, 6, 3, 1]
    result = binary_search(array_2, 9)  # The array needs to be sorted first
    print(result)

    array_2.sort()  # Sorting array_2
    print(array_2)  # Printing the sorted array
    result = binary_search(array_2, 9)
    print(result)

