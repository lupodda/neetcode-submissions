class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, index):
            if index == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(subset, index+1)
            
            subset.pop()
            backtrack(subset, index+1)


        backtrack([], 0)
        return res
        