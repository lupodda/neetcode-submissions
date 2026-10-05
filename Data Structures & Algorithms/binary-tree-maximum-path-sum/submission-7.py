# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max_sum = float("-inf")

        def dfs(node):
            nonlocal global_max_sum

            if not node:
                return 0

            left_max_sum = max(dfs(node.left),0)
            right_max_sum = max(dfs(node.right),0)

            local_max_sum = left_max_sum + node.val + right_max_sum

            global_max_sum = max(global_max_sum, local_max_sum)

            return max(left_max_sum, right_max_sum) + node.val

        dfs(root)
        return global_max_sum


        