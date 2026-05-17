# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder is telling us the value of the current node to construct
        # inorder is telling us the structure of the tree
        preindex = inindex = 0

        def dfs(limit):
            nonlocal preindex, inindex
            
            if preindex == len(preorder):
                return None
                
            if inorder[inindex] == limit:
                inindex+=1
                return None

            node = TreeNode(preorder[preindex])
            preindex +=1
            node.left = dfs(node.val)    
            node.right = dfs(limit)

            return node

        return dfs(float("inf"))

            

            

        