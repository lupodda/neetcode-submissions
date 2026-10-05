class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_prev=rob_prev_prev=0

        for house_money in nums:
            new_rob=max(rob_prev, house_money+rob_prev_prev)
            rob_prev_prev=rob_prev
            rob_prev=new_rob

        return rob_prev
        