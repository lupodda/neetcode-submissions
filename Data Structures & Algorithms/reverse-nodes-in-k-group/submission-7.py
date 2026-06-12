# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # find the kth node
        # cut the sublist
        # revert the sublist
        # attach the sublist
        # advance the pointers
        # prev | group_start kth | group_next
        # prev | new_head group_start | group_next

        def revert(node):
            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        dummy = ListNode(0,head)
        prev = dummy

        while True:
            kth = prev
            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            group_next = kth.next
            kth.next = None
            group_start = prev.next
            new_head = revert(group_start)

            group_start.next = group_next
            prev.next = new_head #forgot
            prev = group_start





            
        