from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequences = defaultdict(int)
        heap = []

        for num in nums:
            frequences[num]+=1
        
        for key, frequence in frequences.items():
            heapq.heappush(heap, (frequence, key))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [key for freq, key in heap]
            
