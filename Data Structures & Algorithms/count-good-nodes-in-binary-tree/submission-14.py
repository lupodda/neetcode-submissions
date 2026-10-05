# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # visit all the node with dfs
        # dfs takes as input the node and the max_val
        # increment the number of good nodes if the current node has a value bigger than the max_val
        # return the number of good nodes

        good_nodes = 0

        def dfs(node, max_val):
            nonlocal good_nodes
            if not node:
                return

            if node.val >= max_val:
                good_nodes+=1

            max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        return good_nodes
        