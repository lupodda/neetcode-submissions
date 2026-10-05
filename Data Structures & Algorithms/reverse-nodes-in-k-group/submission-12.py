# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # group_prev | head  tail | group_next
        # group_prev | tail  head | group_next

        # find the kth node
        # cut
        # revert the sublist 
        # attach
        # update the pointers
        def revert_list(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        dummy = ListNode(0, head)
        prev = dummy

        while True:
            temp = prev

            for _ in range(k):
                if temp.next:
                    temp = temp.next
                else:
                    return dummy.next

            group_next = temp.next
            group_prev = prev
            first = prev.next
            tail = temp

            group_prev.next = None
            tail.next = None

            new_head = revert_list(first)
            group_prev.next = new_head
            first.next = group_next

            prev = first

    
                

        