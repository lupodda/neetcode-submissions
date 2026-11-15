"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create an hashmap that maps node to copy
        #initialize a queue with the first node
        # iterate on the queue
        # pop
        # add the popped node to visited
        # check the neighbors of the original node
        # append the neighbors to the queue if they are not in visited
        # create a copy of the neighbors and append it to the original node
        #return the value of the hashmap of the first node

        def copy_node(node):
            copy = Node()
            copy.val = node.val

            return copy

        if not node:
            return None
        
        queue = deque([node])
        copy = copy_node(node)
        node_to_copy = {node:copy}

        while queue:
            element = queue.popleft()
            # visited.add(element)
            for nei in element.neighbors:
                if nei not in node_to_copy:
                    queue.append(nei)
                    node_to_copy[nei] = copy_node(nei)
                node_to_copy[element].neighbors.append(node_to_copy[nei])

        return node_to_copy[node]


