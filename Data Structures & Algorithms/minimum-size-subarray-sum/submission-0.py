class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')
        sequence_sum = 0
        
        for right, num in enumerate(nums):
            sequence_sum += num

            while sequence_sum >= target:
                min_length = min(min_length, right-left+1)

                sequence_sum -= nums[left]
                left += 1
            

        return min_length if min_length < float('inf') else 0
            



