from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequences = defaultdict(int)
        heap = []

        for num in nums:
            frequences[num]+=1
        
        for key, frequence in frequences.items():
            if len(heap) >= k:
                min_freq = heapq.heappop(heap)
                if frequence > min_freq[0]:
                    heapq.heappush(heap, (frequence,key))
                else:
                    heapq.heappush(heap, min_freq)
            else:
                heapq.heappush(heap,(frequence,key))
        return [key for freq, key in heap]
            
