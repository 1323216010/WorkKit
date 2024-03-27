def binary_search_v2_modified(nums, target):
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left <= right:  # 修改终止条件为 left <= right
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# tests = [
#     ([], 1),                  # 空数组
#     ([1], 0),                 # 单元素数组，目标值不存在
#     ([1], 1),                 # 单元素数组，目标值存在
#     ([1, 2, 3, 4, 5], 3),     # 多元素数组，目标值存在
#     # ([1, 2, 3, 4, 5], 6),     # 多元素数组，目标值不存在
#     ([1, 2, 3, 4, 5, 6], 3),  # 偶数长度数组，目标值存在
#     # ([1, 2, 3, 4, 5, 6], 7)   # 偶数长度数组，目标值不存在
# ]

tests = [
    ([1, 2, 3, 4, 5], 6),     # 多元素数组，目标值不存在
    ([1, 2, 3, 4, 5, 6], 7)   # 偶数长度数组，目标值不存在
]


for nums, target in tests:
    result = binary_search_v2_modified(nums, target)
    print(f"nums: {nums}, target: {target}, result: {result}")
