class Solution:
    def rob(self, nums: List[int]) -> int:
        # define a helper function to get the max amount to rob in a list of houses
        # return the maximum between nums[0], the max amount taking the last but not the first and taking the first but not the last house

        return max(nums[0], self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))
        
    def rob_linear(self, nums):
        rob_prev_prev = rob_prev = 0

        for house in nums:
            new_rob = max(rob_prev, house+rob_prev_prev)
            rob_prev_prev= rob_prev
            rob_prev = new_rob

        return rob_prev
        