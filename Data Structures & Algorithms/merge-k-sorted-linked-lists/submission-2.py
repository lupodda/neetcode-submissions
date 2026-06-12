# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other : self.val < other.val
        heap = []
        for head in lists:
            heapq.heappush(heap, head)

        dummy = ListNode()
        prev = dummy

        while heap :
            node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, node.next)
            prev.next = node
            prev = node

        return dummy.next
        



        