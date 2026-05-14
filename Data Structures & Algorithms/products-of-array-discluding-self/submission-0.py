class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res












        # n = len(nums)
        # prefix=[1]*n
        # postfix=[1]*n
        # res=[]
        # for i in range(1, n):
        #     prefix[i]=prefix[i-1]*nums[i-1]
        # for i in range(n-2, -1, -1):
        #     postfix[i]=postfix[i+1]*nums[i+1]
        # for i in range(n):
        #     res.append(prefix[i]*postfix[i])
        # return res


        # looping over nums form the beginning to the end
        # store the cumulative of the multiplication up the current index in an array (all the elements on the left ogf the current element)
        # for the fist value the left id equal to 1 becuse it is the neutral element of the multiplication
        # 
        # loop over nums from the end to the beginning
        # we store the cumulative of the multiplications up to the current index in the array (excluded)
        # for the last value we store 1
        #
        # then for each element we multiply the current element of the right array and the left array
        # we store the result in a separate array

        # whenever i can initialize arrays with default values it is better so that i dont have to deal with default cases
        # looping multiple times on the same array does not add complexity 
        # it can be useful to loop on the earry to exract features
        # keep focusing on edge cases!!!! (use the 1 at the beginnning and at the end)
        # 
        # 
       
