from top_k_frequent_elements import Solution

def test_ex1():
    solution = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    answer = solution.topKFrequent(nums, k)
    assert answer == [1, 2]

def test_ex2():
    solution = Solution()
    nums = [1]
    k = 1
    answer = solution.topKFrequent(nums, k)
    assert answer == [1]