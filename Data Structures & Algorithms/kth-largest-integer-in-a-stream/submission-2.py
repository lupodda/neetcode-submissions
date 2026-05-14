
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums)>k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
            print(self.nums)
        return self.nums[0]

    # MAIN TAKEAWAYS
    # Heap is not a sorted list, we cannot access the kth element thinking is the kth largest
    # always check corner cases like empty lists, but really checking going thruogh an example
    # heap[0] is the top of the heap but heap[-1] is not the biggest or smallest elemetn for min and max heap respectively
    # remember SELF!!!

        
