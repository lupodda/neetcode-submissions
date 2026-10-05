# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        global_max_path_sum = float("-inf")

        def dfs(node):
            nonlocal global_max_path_sum
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            local_max_path_sum = left+node.val+right
            global_max_path_sum = max(global_max_path_sum, local_max_path_sum)

            return max(left+node.val, node.val+right)

        dfs(root)
        return global_max_path_sum
        # dfs computes the local max path sum for the current subtree