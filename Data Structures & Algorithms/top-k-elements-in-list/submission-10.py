from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []

        for n in nums:
            freq[n] += 1

        for key, f in freq.items():
            heapq.heappush(heap, (-f,key))

        res = []
        for _ in range(k):
            f,key = heapq.heappop(heap)
            res.append(key)

        return res

        

