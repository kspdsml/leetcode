from group_anagrams import Solution

def test_ex1():
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert solution.groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]] 
    # or \
    # [["bat"], ["ate","eat","tea"], ["nat","tan"]] or [["nat","tan"], ["bat"], ["ate","eat","tea"]] or \
    # [["nat","tan"], ["ate","eat","tea"], ["bat"]] or [["ate","eat","tea"], ["bat"], ["nat","tan"]] or \
    # [["ate","eat","tea"], ["nat","tan"], ["bat"]]

# def test_ex2():
#     solution = Solution()
#     strs = [""]
#     assert solution.groupAnagrams(strs) == [[""]]

# def test_ex3():
#     solution = Solution()
#     strs = ["a"]
#     assert solution.groupAnagrams(strs) == [["a"]]