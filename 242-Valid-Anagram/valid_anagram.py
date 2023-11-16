class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_map = {}
        
        for i in range(len(s)):
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1
            
            if t[i] in freq_map:
                freq_map[t[i]] -= 1
            else:
                freq_map[t[i]] = -1
        if max(freq_map.values()) == 0:
            return True
        return False