# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # convert the bst in a list and take the kth element

        tree_list = []

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            tree_list.append(node.val)
            dfs(node.right)

        dfs(root)
        print(tree_list)
        return tree_list[k-1]