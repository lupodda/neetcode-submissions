class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left +=1
                right -= 1
        
        k %= len(nums)
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

        # MAIN TAKEWAYS
        # keep in mind it's possible to revese a list in place
        # Look for blocks in the reversed list
        # passing the pointers avoisd duplicating the list
        # look at the contraints for the limits (modulo operator)

        # TIME & SPACE COMPLEXITY
        # time: O(n)
        # space: O(1)

