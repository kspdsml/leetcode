from length_of_longest_substring import Solution

def test_ex1():
    solution = Solution()
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3

def test_ex2():
    solution = Solution()
    s = "bbbbb"
    assert solution.lengthOfLongestSubstring(s) == 1

def test_ex3():
    solution = Solution()
    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3
