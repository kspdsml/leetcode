from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        heap = []
        heapq.heapify(heap)
        for element, frequency in freq_map:
            heapq.heappush(heap, (frequency, element))
            if len(heap) > k:
                heapq.heappop(heap)