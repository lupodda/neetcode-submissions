# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node):
            nonlocal max_path_sum

            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # compute the max_path_sum WITH splitting
            max_path_sum = max(max_path_sum, left_max + right_max + node.val)

            #return the max_path WITHOUT splitting
            return node.val + max(left_max, right_max)

        dfs(root)
        return max_path_sum

        
    #    3
    #   / \
    #  9   20
    #     /  \
    #    15   7
    #    /
    #   3
    # max path sum 47
    # compute the max_path_sum of the left and right subtrees + node.val


