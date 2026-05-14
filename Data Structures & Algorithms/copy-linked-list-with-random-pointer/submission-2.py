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
        # Loop over the likend likst and initialize and hashmap with the old nodes as key and a new node as value wiht the same value of the node
        # loop over the hash map and point the pointers of the new nodes to the values of the hashmap
        # be careful to also map None:None

        hash_map = {None: None}
        temp = head
        while temp:
            hash_map[temp] = Node(temp.val)
            temp = temp.next

        for old_node, new_node in hash_map.items():
            if old_node and new_node:
                new_node.next = hash_map[old_node.next]
                new_node.random = hash_map[old_node.random]            
        
        return hash_map[head]
        