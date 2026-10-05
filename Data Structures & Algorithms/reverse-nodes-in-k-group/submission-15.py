# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev
            
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            kth = prev
            for _ in range(k):
                kth= kth.next
                if not kth:
                    return dummy.next

            group_start = prev.next
            group_next = kth.next

            kth.next = None

            new_head = reverse(group_start)

            prev.next = new_head
            group_start.next = group_next

            prev = group_start

        