class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        
        for i,n in enumerate(nums):
            diff=target- n
            if diff not in hash_map:
                hash_map[n]=i
            else:
                return [hash_map[diff],i]