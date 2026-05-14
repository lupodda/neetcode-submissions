# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # I iterate over the full list to count how many elements are in the list
        # 1) Find the head of the second list (second half)
        # 2) Revert the second list
        # 3) merge the two lists alternatively

        # 1) find the half of the list
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        # 2) revert the second half
        prev=None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        # 3) merge the two lists alternatively
        first_half, second_half = head, prev
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2


        




