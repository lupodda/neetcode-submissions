# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # overwrite the lt method for ListNode
        #loop over the list
        # push the first element in each list in the heap
        # initialize a dummy node
        # assign temp to dummy
        # while heap pop from the heap
        # assign temp.next to the popped node
        #advance temp
        #return dummy.next
        ListNode.__lt__ = lambda self, other : self.val < other.val
        heap =[]

        for head in lists:
            heapq.heappush(heap, head)

        dummy = ListNode()
        temp= dummy

        while heap:
            node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, node.next)
            
            temp.next = node
            temp=temp.next

        return dummy.next

            

        