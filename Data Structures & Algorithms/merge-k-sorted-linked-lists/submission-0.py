# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head)
                head = head.next

        dummy = ListNode()
        temp = dummy

        while heap:
            temp.next = heapq.heappop(heap)
            temp = temp.next
        
        return dummy.next

        