# recursive solution
from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        # @cache
        def dfs(house, memo):
            if house in memo:
                return memo[house]

            if house >= len(nums):
                memo[house] = 0
                return memo[house]

            memo[house] = max(dfs(house+1, memo), nums[house]+dfs(house+2, memo))
            return memo[house]

        return dfs(0, memo)

        