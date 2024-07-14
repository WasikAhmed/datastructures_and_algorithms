def bubble_sort(arr: list[int]):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    arr = [475, 149, 560, 379, 300, 339, 692, 291, 307, 283]
    bubble_sort(arr)
    print(arr)
