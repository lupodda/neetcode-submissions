class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # define two different empty lists res and subset
        # defien a backtrack dunction taking a start index and the current sum as parameters
        # if the current sum is greater than the target return 
        # if the current sum is equal to the target append to the results list a copu of the subset
        # for all the elements in the list append the current element in the subset
        # call the backtrack function
        # remove the element from the subset
        #call backtrack and return res

        res = []
        subset =[]

        def backtrack(start, current_sum):
            if current_sum == target:
                res.append(subset.copy())
                return
            if current_sum > target:
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, current_sum+nums[i])
                subset.pop()

        backtrack(0, 0)
        return res










        