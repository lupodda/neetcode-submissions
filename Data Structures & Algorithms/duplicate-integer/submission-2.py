class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_map = set()

        for _, n in enumerate(nums):
            if n not in set_map:
                set_map.add(n)
            else:
                return True
        
        return False