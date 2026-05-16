# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def dfs(node, max_path_node):
            nonlocal good_nodes
            if not node:
                return
            
            if node.val >= max_path_node:
                good_nodes+=1
            
            max_path_node = max(max_path_node, node.val)
            dfs(node.left, max_path_node)
            dfs(node.right, max_path_node)

        dfs(root, float("-inf"))
        return good_nodes
        