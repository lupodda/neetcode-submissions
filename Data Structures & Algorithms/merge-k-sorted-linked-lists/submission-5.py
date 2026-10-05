# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # overwrite the lt method for ListNode
        # initialize an empty heap with the first eleemnt of each linked list
        # pop from the heap
        # append the node to the result linked list
        # push in the heap the next node if there it exists
        # return the result linked list

        ListNode.__lt__ = lambda self, curr: self.val < curr.val
        heap = []
        for head in lists:
            heapq.heappush(heap, head)

        dummy = ListNode()
        temp = dummy

        while heap:
            node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next

        