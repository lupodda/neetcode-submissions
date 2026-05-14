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
        
        if self.areTreesEqual(root,subRoot):
            return True

        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        return left or right
                


        
    # implement a function that takes two trees and retrun True if they are equal
    # if the trees are not the same, check if the children are equal to the tree
    #   A or B
    # true,true -> true
    # true,flase -> true
    # false,true -> true
    # false, flase -> false

    def areTreesEqual(self, t1, t2):
        if not t1 and not t2:
            return True

        if t1 and t2 and t1.val == t2.val:
            left = self.areTreesEqual(t1.left,t2.left)        
            right = self.areTreesEqual(t1.right,t2.right)
        
            return left and right
        else:
            return False




