# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initialize a global list to store the results:
        # if the len of the results list is smaller than the depth of the current node append an empty list
        # append the value of the node to the list indexed at the depth of the node
        # return results list

        res = []

        def dfs(node, depth):
            if not node:
                return
            
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return res

        #MAIN TAKEAWAYS
        # Always reason before coding
        # Always go throusg a dry run before
        # ALWAYS remember to invoke the recursive steps
            
        