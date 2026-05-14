class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == [] or len(nums)==1:
            return False

        nums.sort()

        previous = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == previous:
                return True
            else:
                previous = nums[i]
        return False
            
        