def selection_sort(arr: list[int]):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    arr = [80, 33, 12, 65, 5]
    selection_sort(arr)
    print(arr)
