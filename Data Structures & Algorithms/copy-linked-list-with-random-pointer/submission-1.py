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
        # 1) loop over the list and sotore each node as jey in an ahshmap  and an empty node as value
        # 2) loop over the list again and for each node acess the new empty node in the hasmap and point the corresponding pointers to tge pointers of the empty node

        temp=head
        old_to_new = {None:None}

        while temp:
            new_node = Node(temp.val)
            old_to_new[temp] = new_node
            temp=temp.next

        temp=head

        while temp:
            current_node=old_to_new[temp]
            current_node.next = old_to_new[temp.next]
            current_node.random = old_to_new[temp.random]
            temp=temp.next
        
        return old_to_new[head]


        