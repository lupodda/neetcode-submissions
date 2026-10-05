# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True

            if node.val <= lower_bound:
                return False
            elif node.val >= upper_bound:
                return False
            else:
                return dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound)

        return dfs(root, float("-inf"), float("inf"))

    # MAIN TAKEAWAYS: 
    # dfs gives bounds to hte children
    # we return false if the current node is out of bounds
    # else we check that both the left and the right children are within the new bounds
    # we compute the max and the min values implicitly


    # Time and Space complexity
    # time: O(n)
    # space: O(h) -> O(n)