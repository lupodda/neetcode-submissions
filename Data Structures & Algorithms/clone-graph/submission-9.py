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
        if not node:
            return None

        queue = deque([node])
        node_to_copy = {node:Node(node.val)}

        while queue:
            current = queue.popleft()

            for nei in current.neighbors:
                if nei not in node_to_copy:
                    node_to_copy[nei] = Node(nei.val)
                    queue.append(nei)
                node_to_copy[current].neighbors.append(node_to_copy[nei])

        return node_to_copy[node]
        