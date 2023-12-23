from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in index_map.keys():
                return [i, index_map[compliment]]
            else:
                index_map[nums[i]] = i