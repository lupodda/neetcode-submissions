class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # initialize and empty list tostore the results
        # define a backtrack function with index as parameter
        # if index is equal to the length of nums it means the permutation is finished
        # for each element in nums from index on take tha swapped elements as permutation 
        # call backtrack incrasing the index
        # swap back the two numbers to go back to the original definition

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