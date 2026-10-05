class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        n = len(nums)

        def binary_search_left(nums, target):
            left = 0
            right = len(nums)-1

            while left < right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid
            return left

        for i in range(n):
            index = binary_search_left(res, nums[i])

            if res and nums[i] <= res[index]:
                res[index] = nums[i]
            else:
                res.append(nums[i])

        return len(res)