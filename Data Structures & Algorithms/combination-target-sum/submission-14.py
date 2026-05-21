class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(subset, current_sum, start):
            if current_sum > target:
                return

            if current_sum == target:
                res.append(subset.copy())
                return

            for i in range(start, len(nums)):
                subset.append(nums[i])
                current_sum += nums[i]
                backtrack(subset, current_sum, i)
                subset.pop()
                current_sum -= nums[i]

        backtrack([], 0, 0)
        return res

        