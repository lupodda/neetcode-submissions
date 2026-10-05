class Solution:
    def rob(self, nums: List[int]) -> int:
        # define two variables rob_prev and rob_prev_prev both =0
        # for each house money in nums either we take the current one plus the one after the next one or we take the next one
        # the new_rob is equal to the meximum of the two
        # update the balue of rob_prev_prev and rob_prev

        rob_prev_prev = rob_prev = 0

        for house in nums:
            new_rob = max(rob_prev, house + rob_prev_prev)
            rob_prev_prev = rob_prev
            rob_prev = new_rob

        return rob_prev

        