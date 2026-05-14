class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def backtrack(start):
            if sum(subset)>target:
                return 
            elif sum(subset) == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i)
                subset.pop()

        backtrack(0)
        return res
        