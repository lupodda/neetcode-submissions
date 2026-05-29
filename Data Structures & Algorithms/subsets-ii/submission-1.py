class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(subset, index):
            if index == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(subset, index+1)

            subset.pop()
            while index+1<len(nums) and nums[index] == nums[index+1]:
                index+=1
            backtrack(subset, index+1)

        backtrack([], 0)
        return res
