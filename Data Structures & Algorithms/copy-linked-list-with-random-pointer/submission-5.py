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
        node_to_node = {None:None}
        temp = head

        while temp:
            val= temp.val
            node_to_node[temp] = Node(val)
            temp = temp.next

        temp = head
        while temp:
            copied_node = node_to_node[temp]
            copied_node.next = node_to_node[temp.next]
            copied_node.random = node_to_node[temp.random]
            temp = temp.next

        return node_to_node[head]

        