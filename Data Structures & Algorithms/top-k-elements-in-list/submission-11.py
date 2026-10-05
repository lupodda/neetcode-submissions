from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []

        for n in nums:
            freq[n] += 1

        for key, f in freq.items():
            heapq.heappush(heap, (f,key))

            if len(heap)>k:
                heapq.heappop(heap)

        return [key for f, key in heap]

        

