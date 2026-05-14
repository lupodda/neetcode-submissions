class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a nums_set
        # for each element in nums_set while the previous element in numset increase the current sequence length
        # check if the current length is the maximum sequence length
        # return max seq length

        max_seq_length = 0
        nums_set = set(nums)

        for i in nums_set:
            current_seq_length = 1
            previous = i-1
            while previous in nums_set:
                current_seq_length+=1
                previous -= 1
            
            max_seq_length = max(max_seq_length, current_seq_length)

        return max_seq_length
        