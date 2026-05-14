class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # initialize two empty lists on for results and one for subset
        # sort the candidates list so that duplicates are one after the other
        # define a backtrack function with start and current_sum as paramters
        # if the current sum is bigget than the target return
        # if the current sum is equal to the target append to results
        # for all the elements in candidaets
        # if the current element is equal to the previous continue
        # append the current element to the subset
        # call backtrack
        # remove the lement from the subset
        # call backtrack and return res

        res = []
        subset = []

        candidates.sort()
        #candidates = [9,2,2,4,6,1,5], target = 8
        #candidates = [1,2,2,4,5,6,9], target = 8

        def backtrack(start, current_sum):
            if current_sum > target:
                return
            if current_sum == target:
                res.append(subset.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if current_sum > target:
                    break
                
                subset.append(candidates[i])
                backtrack(i+1, current_sum+candidates[i])
                subset.pop()

        backtrack(0, 0)
        return res
                












        