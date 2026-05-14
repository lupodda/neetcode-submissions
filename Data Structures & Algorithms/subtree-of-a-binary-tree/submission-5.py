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
        
        same_trees = self.sameTrees(root,subRoot)

        if same_trees:
            return True
        else:
            same_left = self.isSubtree(root.left, subRoot)
            same_right = self.isSubtree(root.right, subRoot)

            return same_left or same_right


        

    def sameTrees(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        if t1.val == t2.val:
            left = self.sameTrees(t1.left, t2.left)
            right = self.sameTrees(t1.right, t2.right)
            return left and right

        else:
            return False
            


        