from product_of_array_except_self import Solution


def test_ex1():
    solution = Solution()
    nums = [1, 2, 3, 4]
    assert solution.productExceptSelf(nums) == [24, 12, 8, 6]


def test_ex2():
    solution = Solution()
    nums = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf(nums) == [0, 0, 9, 0, 0]
