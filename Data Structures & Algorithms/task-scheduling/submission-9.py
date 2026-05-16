from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        cycles = 0
        queue = deque()
        heap = []

        for freq in frequencies.values():
            heapq.heappush_max(heap, freq)

        while heap or queue:
            cycles += 1
            if heap:
                task_freq = heapq.heappop_max(heap)
                task_freq -= 1

                if task_freq > 0:
                    queue.append((task_freq, cycles+n))

            if queue and queue[0][1] <= cycles:
                task_freq, _ = queue.popleft()
                heapq.heappush_max(heap, task_freq)

        return cycles

                

        

        