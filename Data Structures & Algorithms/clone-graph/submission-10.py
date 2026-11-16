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
        def dfs(node): # 
            if node in node_to_copy:
                return node_to_copy[node]

            node_to_copy[node] = Node(node.val)
            for nei in node.neighbors:
                # if nei not in node_to_copy:
                #     node_to_copy[nei] = Node(nei.val)
                    
                node_to_copy[node].neighbors.append(dfs(nei))

            return node_to_copy[node]

        if not node:
            return None

        node_to_copy = {}
        # node_to_copy = {node:Node(node.val)}

        return dfs(node)



        