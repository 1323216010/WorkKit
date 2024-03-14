def binary_search_v3(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


nums = [1, 2, 4, 5, 6, 8, 9]
target = 8
print(binary_search_v3(nums, target))  # 输出：5