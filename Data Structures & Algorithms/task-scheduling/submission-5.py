from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        heap = []
        queue = deque()
        current_time = 0

        for freq in frequencies.values():
            heapq.heappush_max(heap, freq)

        while heap or queue:
            current_time+=1
            if heap:
                freq_task = heapq.heappop_max(heap)
                freq_task-=1
                if freq_task > 0:
                    queue.append((freq_task, current_time+n))

            if queue and queue[0][1] <= current_time:
                heapq.heappush_max(heap, queue.popleft()[0])

        return current_time

                




        