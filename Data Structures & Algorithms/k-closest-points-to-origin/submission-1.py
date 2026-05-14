import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # initialize a maxheap
        # loop over the points
        # compute the disance from the origin for each point
        # store a pair with (distance, [x,y]) in the heap
        # if the length of the heap > k pop from it
        # return a list of the [1] elements for each element in the heap

        heap = []
        for xi, yi in points:
            distance = xi**2 + yi**2
            heapq.heappush_max(heap, (distance, [xi,yi]))

            if len(heap) > k:
                heapq.heappop_max(heap)
        
        return [coords for _ , coords in heap]




        