from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequences = Counter(tasks)
        heap=[]
        queue = deque()

        # max_heap = list(freq.values())
        # heapq.heapify_max(max_heap)     
        for freq in frequences.values():
            heapq.heappush_max(heap, freq)

        current_time = 0
        while heap or queue:
            current_time+=1
            if heap:
                f = heapq.heappop_max(heap)
                f-=1
                if f > 0:
                    queue.append((f, current_time+n))

            if queue and queue[0][1] == current_time:
                f, _ = queue.popleft()
                heapq.heappush_max(heap, f)

        return current_time


        