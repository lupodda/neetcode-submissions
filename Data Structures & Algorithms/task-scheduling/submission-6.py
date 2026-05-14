from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # compute the frequencies of the tasks
        # push the frequencies in a max heap
        # while there are elements in the heap or in the queue
        # increment the number of cycles
        # if heap pop form max heap and decrement the frequence
        # push in the queue
        # if queue pop from it if the first task can be executed
        # return cycles

        frequencies = Counter(tasks)
        heap = []
        queue = deque()
        cycles = 0

        for freq in frequencies.values():
            heapq.heappush_max(heap, freq)

        while heap or queue:
            cycles+=1
            if heap:
                freq = heapq.heappop_max(heap)
                freq -= 1
                if freq > 0:
                    queue.append((freq, cycles+n))
                    
            if queue and queue[0][1] <= cycles:
                available_taks = queue.popleft()[0]
                heapq.heappush_max(heap, available_taks)

        return cycles

        # main takeaways remember to append in the queue ONLY if freq is > 0
        # the avalilable time is <= than cycles!!!!


