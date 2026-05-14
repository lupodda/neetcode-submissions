class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,3,0,4,5]
        # create a set
        # loop over the set
        # for each start of the sequence increment the counter 
        # check whether the nex num is in the set
        # take the maximum counter wrt all the start of sequences
        set_nums = set(nums)
        max_seq = 0
        for current_num in set_nums:
            if current_num-1 not in set_nums:
                seq_len = 0
                while current_num in set_nums:
                    current_num += 1
                    seq_len += 1
                max_seq = max(max_seq, seq_len)

        return max_seq
        
