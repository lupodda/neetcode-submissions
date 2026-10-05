# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            
        # The root of the tree is always the first element in preorder
        # The numbers on the left of the current element ar ein the left subtree and those on the right ar ein the right subtree
        # I can find the index of the seeked number with list.index(number)
        # use inindex and preindex but i don't remember how...
        # 
        if len(preorder) <=0:
            return None

        preindex = 0

        node = TreeNode(preorder[preindex])

        inindex = inorder.index(node.val)

        node.left = self.buildTree(preorder[1:inindex+1], inorder[:inindex])
        node.right = self.buildTree(preorder[inindex+1:], inorder[inindex+1:])
        return node
        
        #            0,1,2,3              0,1,2,3
        #preorder = [1,2,3,4], inorder = [2,1,3,4]
        # preindex   0 1 2
        # inindex    1 0 2

