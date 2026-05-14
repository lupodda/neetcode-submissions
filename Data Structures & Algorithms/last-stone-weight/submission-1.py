import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones)>1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x < y:
                heapq.heappush_max(stones, y-x)
            elif y < x:
                heapq.heappush_max(stones, x-y)
                        
        return heapq.heappop_max(stones) if stones else 0

        