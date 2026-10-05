# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_list(head):
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

        # prev | group_start   kth      | group_next
        # prev | new_head   group_start | group_next
        while True:
            kth = prev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_start = prev.next
            group_next = kth.next

            kth.next = None
            prev.next = None

            new_head = reverse_list(group_start)
            prev.next = new_head
            group_start.next = group_next

            prev = group_start

            

            

        