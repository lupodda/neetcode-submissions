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
        #go through the linked list and stor a dict with node:empty node
        #go stroughbthe linked ilst and collect the pointers

        node_to_node={None:None}

        temp=head
        while temp:
            node_to_node[temp]=Node(temp.val)
            temp=temp.next

        temp=head
        while temp:
            node_to_node[temp].next=node_to_node[temp.next]
            node_to_node[temp].random=node_to_node[temp.random]
            temp=temp.next

        return node_to_node[head]

        