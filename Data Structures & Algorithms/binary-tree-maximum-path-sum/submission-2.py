# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # initiallize max_path_sum to -inf or to root.val
        # define dfs with a node as input
        # compute and return max_path_sum with splitting
        # compute the max_path sum without splitting
        # return max_path sum

        max_path_sum = root.val

        def dfs(node):
            nonlocal max_path_sum

            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            path_sum = left_max + node.val + right_max
            max_path_sum = max(max_path_sum, path_sum)

            return node.val + max(left_max, right_max)

        dfs(root)
        return max_path_sum









        