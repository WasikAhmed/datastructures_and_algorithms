def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    arr = [401, 322, 207, 107, 139, 723, 739, 252, 259, 330]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
