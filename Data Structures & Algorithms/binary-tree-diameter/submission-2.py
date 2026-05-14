# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_max_height = self.maxHeight(root.left)
        right_max_height = self.maxHeight(root.right)

        diameter = left_max_height + right_max_height

        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))

        return max(diameter, sub)

    def maxHeight(self, root):
        if not root:
            return 0
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)

        return 1 + max(left_height, right_height)

