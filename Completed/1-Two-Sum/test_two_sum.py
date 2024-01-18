from two_sum import Solution

def test_ex1():
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1] or [1, 0]

def test_ex2():
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2] or [2, 1]

def test_ex3():
    solution = Solution()
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1] or [1, 0]