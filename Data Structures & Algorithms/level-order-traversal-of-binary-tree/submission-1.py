# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node, dept):
            if not node: 
                return None

            if len(res) == dept:
                res.append([])

            res[dept].append(node.val)
            dfs(node.left, dept+1)
            dfs(node.right, dept+1)

        dfs(root, 0)
        return res

        

        