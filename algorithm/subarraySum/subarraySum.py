def subarraySum(nums, k):
    mp = {0: 1}
    count = 0
    pre = 0
    for x in nums:
        pre += x
        if pre - k in mp:
            count += mp[pre - k]
        mp[pre] = mp.get(pre, 0) + 1
    return count


test_cases = [
    {'nums': [1, 1, 1], 'k': 2, 'expected': 2},
    {'nums': [1, 2, 3], 'k': 3, 'expected': 2},
    {'nums': [-1, -1, 1], 'k': 0, 'expected': 1},
]

for index, test_case in enumerate(test_cases, 1):
    nums, k, expected = test_case['nums'], test_case['k'], test_case['expected']
    result = subarraySum(nums, k)
    print(f"Test Case {index}: Result = {result}, Expected = {expected}")
    assert result == expected, f"Test Case {index} failed: Result = {result}, Expected = {expected}"

print("All test cases passed!")
