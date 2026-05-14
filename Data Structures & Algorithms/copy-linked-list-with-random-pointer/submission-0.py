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

        # 1) loop over the list and create a hashmap with each node as key and an empty node ad value
        # 2.0) loop over the list again and take the node in the hashmap, assign the val to the node as a value
        # 2.1) take the node as next, check for its value in the hashmap and point the 

        temp = head
        hash_map = {None:None}
        while temp:
            hash_map[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            current_node = hash_map[temp]
            current_node.next = hash_map[temp.next]
            current_node.random = hash_map[temp.random]
            temp = temp.next
        
        return hash_map[head]






        