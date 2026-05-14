# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder tells us the order in which roots appear. The FIRST unseen element in preorder is always the next node to create.
        # Inoreder tells us which nodes belong to the left side and which belong to the right side.
        # I need a limit

        pre_index, in_index = 0, 0

        def dfs(limit):
            nonlocal pre_index, in_index
            if pre_index >= len(preorder):
                return None
            if inorder[in_index] == limit:
                in_index+=1
                return None
            
            node = TreeNode(preorder[pre_index])
            pre_index += 1
            node.left = dfs(node.val)
            node.right = dfs(limit)
            return node
        
        return dfs(float("inf"))
            
        