class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict = {}
        for char in s:
            if freq_dict.get(char):
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        for char in t:
            if freq_dict.get(char):
                freq_dict[char] -= 1
            else:
                return False
        if max(freq_dict.values()) == 0:
            return True
        else:
            return False