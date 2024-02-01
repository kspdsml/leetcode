import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        for i in range(1, len(nums)):
            left_product[i] = math.prod(nums[:i])

        for i in range(0, len(nums)-1):
            right_product[i] = math.prod(nums[i+1:])

        output = [left_product[i] * right_product[i] for i in range(len(nums))]

        return output
