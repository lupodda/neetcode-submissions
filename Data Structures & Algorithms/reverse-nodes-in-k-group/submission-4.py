# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # initialize dummy node
        # initialize group_prev

        # While loop always true
        # find the kth node
        # break when not kth node
        # initialize group_next, prev and curr
        # revert the sublist of k nodes
        # attach the revesed list to the next group
        # reinitialize group_prev to point at the previous node of the next group
        # return dummy.next

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.find_kth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            prev = kth.next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth #At the beginnig dummy.next = 3
            group_prev = temp

        return dummy.next


    def find_kth(self, node, k):
        while node and k> 0:
            node = node.next
            k-=1
        return node


        