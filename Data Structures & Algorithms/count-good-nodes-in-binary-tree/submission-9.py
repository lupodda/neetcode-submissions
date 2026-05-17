# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # initialize a counter to 0
        # initialize the max_node_path to the root.val
        # if in the path we find a node with a value bigger than the current max we increment the counter

        good_nodes = 0

        def dfs(node, max_path_node):
            nonlocal good_nodes
            if not node:
                return
            
            if node.val >= max_path_node:
                good_nodes+=1
                max_path_node = node.val
            
            dfs(node.left, max_path_node)
            dfs(node.right, max_path_node)

        dfs(root, root.val)
        return good_nodes
        #time complexity = O(n)
        # space complexity = O(h) recursion stack -> with unbalanced tree h=n else h=log(n)

            

        