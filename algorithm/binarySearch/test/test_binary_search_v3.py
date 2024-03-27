def binary_search_v3_leq(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
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

def binary_search_v3_lt(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
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


tests = [
    ([], 1),                  # 空数组
    ([1], 0),                 # 单元素数组，目标值不存在
    ([1], 1),                 # 单元素数组，目标值存在
    ([1, 2, 3, 4, 5], 3),     # 多元素数组，目标值存在
    ([1, 2, 3, 4, 5], 6),     # 多元素数组，目标值不存在
    ([1, 2, 3, 4, 5, 6], 3),  # 偶数长度数组，目标值存在
    ([1, 2, 3, 4, 5, 6], 7)   # 偶数长度数组，目标值不存在
]

for nums, target in tests:
    result_leq = binary_search_v3_leq(nums, target)
    result_lt = binary_search_v3_lt(nums, target)
    print(f"nums: {nums}, target: {target}, result_leq: {result_leq}, result_lt: {result_lt}")
