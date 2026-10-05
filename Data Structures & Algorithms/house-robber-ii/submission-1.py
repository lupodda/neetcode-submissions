class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        memo = [[-1]*2 for _ in range(len(nums))]

        def dfs(house, flag):
            if house >= len(nums) or (flag and house == len(nums)-1):
                return 0

            if memo[house][flag] != -1:
                return memo[house][flag]


            memo[house][flag] = max(dfs(house+1, flag), 
                                    nums[house]+dfs(house+2, flag or (house == 0)))
            return memo[house][flag]
        
        return max(dfs(0, True), dfs(1, False))

