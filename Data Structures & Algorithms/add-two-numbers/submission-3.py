# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        carry = 0

        dummy = ListNode()
        temp_res = dummy
        while temp1 or temp2 or carry:
            digit1 = temp1.val if temp1 else 0
            digit2 = temp2.val if temp2 else 0

            res = digit1+digit2+carry
            digit = res % 10
            carry = res //10

            temp_res.next= ListNode(digit)

            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
            temp_res = temp_res.next

        return dummy.next
        

            

        