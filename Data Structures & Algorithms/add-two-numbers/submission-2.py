# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize a dummy node
        # initialize carry to 0
        # while there is either a node or carry sum up the nodes value
        # compute the new carry
        # store the result in a new node
        # attach the new node to the current
        #return dummy.next

        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            new_val = l1_val+l2_val+carry
            digit = new_val%10
            carry = new_val//10

            current.next = ListNode(digit)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            current = current.next

        return dummy.next

        