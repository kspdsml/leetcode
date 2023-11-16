from valid_anagram import Solution

def test_ex1():
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t) == True

def test_ex2():
    solution = Solution()
    s = "rat"
    t = "car"
    assert solution.isAnagram(s, t) == False

def test_failed1():
    solution = Solution()
    s = "ac"
    t = "bb"
    assert(solution.isAnagram(s, t) == False)

def test_failed2():
    solution = Solution()
    s = "fe"
    t = "ja"
    assert(solution.isAnagram(s, t) == False)

def test_failed3():
    solution = Solution()
    s = "hqbqo"
    t = "lsnma"
    assert(solution.isAnagram(s, t) == False)