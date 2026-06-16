# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        def revert_list(node):
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

        second_half = revert_list(slow)
    
        temp1 = head
        temp2 = second_half
        while temp1.next and temp2.next:
            next1, next2 = temp1.next, temp2.next
            temp1.next = temp2
            temp2.next = next1
            temp1, temp2 = next1, next2



        
        