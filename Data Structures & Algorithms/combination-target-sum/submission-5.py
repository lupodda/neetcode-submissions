class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #initialize two lists one global and one for subets
        #check the case base when the sum is bigger than the target
        #check the best case when the sum is equal to the target
        # for each ramaining element in the list choose wether to pick it or not
        # invoke backtrack
        res = []
        subset = []

        def backtrack(start):
            if sum(subset) > target:
                return
            elif sum(subset) == target:
                res.append(subset.copy())
                return

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i)
                subset.pop()

        backtrack(0)
        return res
                

        