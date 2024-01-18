from group_anagrams import Solution

def test_ex1():
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert solution.groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]]

def test_ex2():
    solution = Solution()
    strs = [""]
    assert solution.groupAnagrams(strs) == [[""]]

def test_ex3():
    solution = Solution()
    strs = ["a"]
    assert solution.groupAnagrams(strs) == [["a"]]