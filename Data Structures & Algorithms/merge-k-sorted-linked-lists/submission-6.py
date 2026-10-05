# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #loop oveer the lists, for each list push the first element in  min heap
        # once the heap is constucted start popping the first
        ListNode.__lt__ = lambda x, y : x.val < y.val
        
        heap = []

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, head))

        dummy = ListNode()
        temp = dummy
        while heap:
            val, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            temp.next = node
            temp = temp.next

        return dummy.next

    






        