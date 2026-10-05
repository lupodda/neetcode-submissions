class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(start, subset, current_sum):
            if current_sum == target:
                res.append(subset.copy())
                return
            
            elif current_sum > target:
                return
            
            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i, subset, current_sum+nums[i])
                subset.pop()

        backtrack(0, [], 0)
        return res
        