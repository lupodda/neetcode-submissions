class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self, nums):
        rob_prev=rob_prev_prev=0
        for house in nums:
            new_rob=max(rob_prev, house+rob_prev_prev)
            rob_prev_prev=rob_prev
            rob_prev=new_rob
        return rob_prev