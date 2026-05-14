from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequences = Counter(tasks)
        heap=[]
        queue = deque()
        for task,freq in frequences.items():
            heapq.heappush_max(heap, freq)

        current_time = 0
        while heap or queue:
            current_time+=1
            if heap:
                f = heapq.heappop_max(heap)
                f-=1
                if f > 0:
                    queue.append((f, current_time+n))

            while queue and queue[0][1] <= current_time:
                f, available_time = queue.popleft()
                heapq.heappush_max(heap, f)

        return current_time


        