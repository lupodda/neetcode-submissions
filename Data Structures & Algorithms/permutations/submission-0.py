class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, index):
            if index == len(nums):
                res.append(nums.copy())
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(nums, index+1)
                nums[index], nums[i] = nums[i], nums[index]
                
        backtrack(nums, 0)
        return res

        