# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # start a while True
        # find the kth node
        # cut the sublist
        #revert it
        # attach it
        # update pointers

        # prev | group_start kth | group_next
        # prev | new_head group_start | group_next

        def reverse(node):
            prev = None
            temp = node

            while temp:
                temp = node.next
                node.next = prev
                prev = node
                node = temp

            return prev

        dummy = ListNode(0, head)
        temp = dummy
        while True:
            prev = temp
            group_start = temp.next

            for _ in range(k):
                temp = temp.next
                if not temp:
                    return dummy.next
            
            kth = temp
            group_next = kth.next
            kth.next = None

            new_head = reverse(group_start)

            prev.next = new_head
            group_start.next = group_next
            temp = group_start

        # prev | group_start kth | group_next
        # prev | new_head group_start | group_next



        




        