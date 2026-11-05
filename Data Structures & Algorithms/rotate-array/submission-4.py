class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,j):
            while i<j:
                 temp=nums[i]
                 nums[i]=nums[j]
                 nums[j]=temp
                 i+=1
                 j-=1


        left=0 
        right=len(nums)-1 
        k%=len(nums)
        reverse(left,right)
        reverse(left, k-1)
        reverse(k, right)
