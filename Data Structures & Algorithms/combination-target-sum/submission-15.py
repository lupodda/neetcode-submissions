class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, index, current_sum):
            if current_sum > target:
                return

            if current_sum == target:
                res.append(subset.copy())
                return
            
            for i in range(index,len(nums)):
                subset.append(nums[i])
                backtrack(subset, i, current_sum+nums[i])
                subset.pop()

        backtrack([], 0, 0)
        return res
            
