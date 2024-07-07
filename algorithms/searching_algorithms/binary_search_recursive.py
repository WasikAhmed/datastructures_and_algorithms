from typing import List

def binary_search_recursive(nums: List, left: int, right: int, value: int) -> int:
    if left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == value:
            return mid
        elif nums[mid] > value:
            return binary_search_recursive(nums, left, mid - 1, value)
        else:
            return binary_search_recursive(nums, mid + 1, right, value)
    else:
        return -1

if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 9, 11, 13, 16, 19, 22]
    
    print(binary_search_recursive(nums, 0, len(nums) - 1, 19))
    print(binary_search_recursive(nums, 0, len(nums) - 1, 3))
    print(binary_search_recursive(nums, 0, len(nums) - 1, 30))
