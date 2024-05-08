# Linear search is a simple search algorithm that
# sequentially checks each element in a list until a match is found or the entire list has been searched.

# The time complexity of the linear search algorithm is O(n)

def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == '__main__':
    array = [5, 3, 8, 4, 2]
    result = linear_search(array, 8)
    print(result)
