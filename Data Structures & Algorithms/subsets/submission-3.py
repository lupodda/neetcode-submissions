class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # define res and subset
        # define backtrack that adds the leaf node and makes two choices to add or not add the current element
        # return res

        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #choosing to add the current element to the subset
            subset.append(nums[i])
            backtrack(i+1)

            #choosing to NOT add the current element to the subset
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res
        