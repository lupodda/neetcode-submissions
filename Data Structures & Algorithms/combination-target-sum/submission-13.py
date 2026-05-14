class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # initialize an empty list res
        # define bacltrack taking start index, current sum subset as parameters
        # define the base case when the current sum is bigger then the target
        # check if the current sum is equal to the target in case add subset to res
        # for each element among the ones in nums append the current element 
        # call backtrack with index i
        # pop the last element

        res = []

        def backtrack(start, current_sum, subset):
            if current_sum > target: # start == len(nums) 
                return

            if current_sum == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(nums)): 
                subset.append(nums[i])
                backtrack(i, current_sum+nums[i], subset)
                subset.pop()

        backtrack(0,0,[])
        return res

        #TIME AND SPACE COMPLEXITY
        # time = n^(t/m) where t is the target, n is the length of nums and m is the smallest element in nums
        # space = t/m 

        # time id given by the maximum recursive depth (t/m) and the braching factor n
        # space is given by the recursion stack which is t/m
        # res has a maximum size of n^(t/m) (number of elements) * t/m the size of the subset in the worst case