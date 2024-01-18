from contains_duplicate import Solution

def test_ex1():
    solution = Solution()
    nums = [1,2,3,1]
    assert solution.containsDuplicate(nums) == True

def test_ex2():
    solution = Solution()
    nums = [1,2,3,4]
    assert solution.containsDuplicate(nums) == False

def test_ex3():
    solution = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    assert solution.containsDuplicate(nums) == True