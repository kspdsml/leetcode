from valid_parentheses import Solution

def test_ex1():
    solution = Solution()
    s = "()"
    assert solution.isValid(s) == True

def test_ex2():
    solution = Solution()
    s = "()[]{}"
    assert solution.isValid(s) == True

def test_ex3():
    solution = Solution()
    s = "(]"
    assert solution.isValid(s) == False