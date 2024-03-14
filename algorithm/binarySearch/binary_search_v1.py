def binary_search_v1(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [1, 2, 4, 5, 6, 8, 9]
target = 5
print(binary_search_v1(nums, target))  # 输出：3