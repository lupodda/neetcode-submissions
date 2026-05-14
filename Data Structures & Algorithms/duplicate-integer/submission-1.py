class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i, n in enumerate(nums):
            if n not in hash_map:
                hash_map[n] = i
            else:
                return True
        
        return False