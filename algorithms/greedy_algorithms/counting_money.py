# Given the value of V BDT and an infinite supply of each of the denominations valued coins/notes,
# The task is to find the minimum number of coins and/or notes needed to make the change

def count(v: int, denominations: list[int]) -> list[int]:
    denominations.sort(reverse=True)
    change = []

    for denomination in denominations:
        while v >= denomination:
            v -= denomination
            change.append(denomination)
    return change


if __name__ == '__main__':
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    v = 269
    print(count(v, denominations))
