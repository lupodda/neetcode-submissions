class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        middle = (right+left)//2 

        while left <= right:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
                middle = (right+left)//2 
            else:
                left = middle + 1
                middle = (right+left)//2 

        return -1

        