# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 1) check the base case: if root == none: True
        # 2) return the height of the left and right subtrees
        # 3) compute the differnece between the two heights
        # 4) return False if diff > 1 else True
        def dfs(node):# it retruns the height of the subtree if it's balanced else -1
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1: return -1
            right = dfs(node.right)
            if right == -1: return -1

            if abs(left-right) > 1:
                return -1

            return 1 + max(left,right)

        height = dfs(root)

        return height != -1



        


        