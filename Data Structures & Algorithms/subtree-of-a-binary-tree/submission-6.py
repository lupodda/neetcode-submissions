# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        same_tree = self.same_tree(root, subRoot)
        if same_tree:
            return True
        else:
            left_subTree=self.isSubtree(root.left, subRoot)
            right_subTree=self.isSubtree(root.right,subRoot)
        

        return left_subTree or right_subTree

    def same_tree(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False
        
        if node1.val==node2.val:
            same_left=self.same_tree(node1.left, node2.left)
            same_right=self.same_tree(node1.right, node2.right)

            return same_left and same_right
        else:
            return False
