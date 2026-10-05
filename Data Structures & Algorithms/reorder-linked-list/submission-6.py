# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        def reverse(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        head2 = reverse(mid)

        curr1 = head
        curr2 = head2
        while curr1 and curr2:
            temp1, temp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1, curr2 = temp1, temp2

            


        