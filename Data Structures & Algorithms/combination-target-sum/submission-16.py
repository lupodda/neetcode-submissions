class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, index, current_sum):
            if current_sum > target:
                return

            if current_sum == target:
                res.append(subset.copy())
                return

            for start in range(index, len(nums)):
                subset.append(nums[start])
                backtrack(subset, start, current_sum + nums[start])
                subset.pop()
        
        backtrack([], 0, 0)
        return res
            
        