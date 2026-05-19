"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_nodes = {}

        def dfs(node):
            if not node:
                return None
            
            if node not in clone_nodes:
                copy = Node(node.val)
                clone_nodes[node] = copy
            
                for neighbor in node.neighbors:
                    copied_neighbor = dfs(neighbor)
                    copy.neighbors.append(copied_neighbor)
                return copy
                
            else:
                return clone_nodes[node]

        
        return dfs(node)
        # for dfs we create and return a copy of the current node
        # 


        