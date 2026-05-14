class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq=0
        
        for n in set_nums:
            if n-1 not in set_nums:
                seq_length=1
                while n+seq_length in set_nums:
                    seq_length+=1
                max_seq= max(max_seq, seq_length)

        return max_seq
