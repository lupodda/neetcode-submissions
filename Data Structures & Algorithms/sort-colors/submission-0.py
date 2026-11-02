class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #[1,0,1,2,0]
        #[0,1,1,2,0]

        return self.selectionsort(nums)

    def selectionsort(self, nums):
        length = len(nums)
        for i in range(length):
            curr = nums[i]
            for j in range(i+1, length):
                if nums[j] < curr:
                    nums[i] = nums[j]
                    nums[j] = curr
                    curr = nums[i]

        return nums

