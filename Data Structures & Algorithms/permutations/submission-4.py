class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # initialize an empty list res
        # define a backtrack function with index and subset as parameters
        # as basecase 
        # fix the index and swap other two elements in the list
        # backtrack 
        # swap the elements again

        res = []
        def backtrack(index):
            if index == len(nums):
                res.append(nums.copy())
                return
            
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index+1)
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(0)
        return res
        #TIME and SPACE complexity
        # time: n*n!
        # space: n
        


        