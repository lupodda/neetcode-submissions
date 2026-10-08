class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_seq=0
        seq=1

        for n in nums:
            seq=1
            previous=n-1

            if previous not in nums_set:
                while n+seq  in nums_set:
                    seq+=1
                    
            max_seq=max(max_seq,seq)

        return max_seq



