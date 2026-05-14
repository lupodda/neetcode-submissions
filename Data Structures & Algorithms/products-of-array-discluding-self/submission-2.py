class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums =   [1,2,4,6]
        # prefix = [1,1,2,8]
        # suffix = [48,24,6,1]
        # output = [48, 24, 12, 8]
        
        # initialize two arrays of ones with length equal to nums: prefix and suffix
        # prefix[i] = prefix[i-1]*nums[i-1] for all i
        # suffix[i] = suffix[i+1]*nums[i+1] for all i in reverse order

        #multiply suffix anf prefix
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        for i in range(len(nums)):
            prefix[i] *= suffix[i]

        return prefix


        