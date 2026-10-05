# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # define a global_max_path_sum variable
        # define a dfs dunction that takes a node and return the max_path_sum without splitting
        # base case in case the nide is none we return 0
        # comput the max path sum for the left and the right subtrees and take the max with 0
        # comupute the local_max_path sum as the sum of the left max path sum, the current node and the right max path sum
        # global_max_path sum is the max between the global_max_path_sum and the local one
        # return global_max_path

        global_max_path_sum = float("-inf")

        def dfs(node):
            nonlocal global_max_path_sum
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            local_max_path_sum = left + node.val + right
            global_max_path_sum = max(global_max_path_sum, local_max_path_sum)

            return max(left, right) + node.val

        dfs(root)
        return global_max_path_sum

