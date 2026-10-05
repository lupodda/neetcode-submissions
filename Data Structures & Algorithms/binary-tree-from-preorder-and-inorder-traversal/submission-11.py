# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        pre_index = 0

        node = TreeNode(preorder[pre_index])
        in_index = inorder.index(node.val)

        node.left = self.buildTree(preorder[1:in_index+1], inorder[:in_index])
        node.right = self.buildTree(preorder[in_index+1:], inorder[in_index+1:])

        return node
        