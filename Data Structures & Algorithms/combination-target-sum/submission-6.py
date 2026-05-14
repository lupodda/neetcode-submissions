class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(start, current_sum):
            if current_sum > target:
                return
            elif current_sum == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, current_sum+nums[i])
                subset.pop()
                
        backtrack(0,0)
        return res
