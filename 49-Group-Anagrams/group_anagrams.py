from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord("a")] += 1
            answers[tuple(count)].append(word)
        return list(answers.values())