class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(depth):
            if depth >= len(nums): #if the element is a leaf in the tree search
                res.append(subset.copy())
                return 
            
            subset.append(nums[depth])
            backtrack(depth+1)

            subset.pop()
            backtrack(depth+1)

        backtrack(0)
        return res
        