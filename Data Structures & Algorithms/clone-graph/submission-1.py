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
            
            if node in clone_nodes:
                return clone_nodes[node]

            copy = Node(node.val)
            clone_nodes[node] = copy
        
            for neighbor in node.neighbors:
                copied_neighbor = dfs(neighbor)
                copy.neighbors.append(copied_neighbor)

            return copy
                
        return dfs(node)
        # Main Takeaways
        # when I have an hashmap I should update it inside the dfs otherwise it doesn't make sense
        # careful when copying the neighbors, first call dfs on the current neighbor and then append it to the copied original node
        # dfs takes a node as input and return the copy of the node and recursively of all its neighbors
        # check if a node has been already copied!!!
        # we use an hashmap to check if a node has been already copied in constant time

        #Time comeplexity: O(n+e)
        # Space complexity O(2n) -> n for recursion stack and n for the hashmap

        