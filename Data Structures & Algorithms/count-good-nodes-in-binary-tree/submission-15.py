# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        max_val_path = float("-inf")

        def dfs(node, max_val_path):
            nonlocal good_nodes
            if not node:
                return

            if node.val >= max_val_path:
                good_nodes+=1
                max_val_path = node.val

            dfs(node.left, max_val_path)
            dfs(node.right, max_val_path)

        dfs(root, max_val_path)
        return good_nodes