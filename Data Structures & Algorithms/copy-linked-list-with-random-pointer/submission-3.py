"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies={None:None}
        temp=head
        while temp:
            copies[temp]=Node(temp.val)
            temp=temp.next
        
        temp=head
        while temp:
            copies[temp].next = copies[temp.next]
            copies[temp].random = copies[temp.random]
            temp=temp.next
        return copies[head]


    
        