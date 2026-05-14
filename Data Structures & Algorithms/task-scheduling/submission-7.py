from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #count the frequences in tasks to take fist the tasks with the highest frequency
        # push the (freq, task) pain in a max_heap
        # pop from the heap and push the executed tasks in a queue qith the available time
        # if the head of the queue is available push it in the heap
        # return the number of cycles

        freq = Counter(tasks)
        queue = deque()
        cycles = 0
        heap = []
        for f in freq.values():
            heapq.heappush_max(heap, f)

        while heap or queue:
            cycles+=1

            if heap:
                task_freq = heapq.heappop_max(heap)
                task_freq -= 1
                if task_freq > 0:
                    queue.append((task_freq, cycles+n))            

            if queue and queue[0][1] <= cycles:
                executable_task = queue.popleft()
                heapq.heappush_max(heap, executable_task[0])

        return cycles

            



        