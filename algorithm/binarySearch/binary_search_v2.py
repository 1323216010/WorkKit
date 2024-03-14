def binary_search_v2(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


nums = [1, 2, 4, 5, 6, 8, 9]
target = 4
print(binary_search_v2(nums, target))  # 输出：2


