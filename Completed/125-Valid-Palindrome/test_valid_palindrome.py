from valid_palindrome import Solution

def test_ex1():
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s) == True

def test_ex2():
    solution = Solution()
    s = "race a car"
    assert solution.isPalindrome(s) == False

def test_ex3():
    solution = Solution()
    s = ""
    assert solution.isPalindrome(s) == True