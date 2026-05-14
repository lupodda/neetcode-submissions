class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # suffix =[48,24,6,1]
        # output =[48,24,12,8]
        # res =   [1,1,2,8] suf =1
        # nums =  [1,2,4,6]
        # output[48,24,12,8]
        # res[i]*suffix
        # suffix *= nums[i]

        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(1, n):
            res[i] = nums[i-1]*prefix
            prefix = res[i]

        print(res)
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *=suffix
            suffix *= nums[i]
        
        return res


        

        