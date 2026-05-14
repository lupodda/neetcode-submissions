# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursevely compute inorder dfs and add the nodes value to the listwith the corresponding depth of the node

        trasversal_list = defaultdict(list)

        def dfs(node, depth):
            if not node:
                return None

            trasversal_list[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root,0)
        return list(trasversal_list.values())
        