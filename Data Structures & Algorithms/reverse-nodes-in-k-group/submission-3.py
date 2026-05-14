# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize a dummy node
        # initialiaze group prev which is the node pervious to each group 
        # find the kth node
        # initialize the first node of the enxt group

        # until we have a kth node then we brek
        # reverse the sublist
        # reinitialize the ointers to the initial node of the next group

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.find_kth(group_prev, k)

            if not kth:
                break

            group_next = kth.next
            prev = kth.next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next


    def find_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -=1

        return node

        