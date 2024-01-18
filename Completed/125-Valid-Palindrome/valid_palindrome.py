class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        s = s.casefold()
        for char in s:
            if (ord(char) > 96 and ord(char) < 123) or (ord(char) > 47 and ord(char) < 58):
                t += char
        p1 = 0
        p2 = len(t) - 1
        while p1 < p2:
            if t[p1] != t[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True