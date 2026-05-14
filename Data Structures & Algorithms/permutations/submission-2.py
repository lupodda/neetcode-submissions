class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #define a single global empty list
        #define backtrack function with insex as parameter
        #index is the current elelment to be selected 
        #if index is eual to the len of nums it means we have finished the oermitathion
        # for all the lementss from index to the end of the list
        # swap nums[i] and nums[index]
        #backtrack with index+1
        # swap again the two numbers
        # call backtrack and return res

        res=[]
        def backtrack(index):
            if index == len(nums):
                res.append(nums.copy())
                return
            
            for i in range(index, len(nums)):
                nums[i],nums[index]=nums[index],nums[i]
                backtrack(index+1)
                nums[i],nums[index]=nums[index],nums[i]

        backtrack(0)
        return res
                
