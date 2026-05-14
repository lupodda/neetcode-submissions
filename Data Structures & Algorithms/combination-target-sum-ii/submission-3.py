class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # initialize two empty lists one for the results and one for the current subset
        # order the candidates list to have duplicates one after the other
        # create a dfs function taking the starting index and the current sum as input
        # if the current sum is bigger than the target, return 
        # if the current sum is equal to the target, append a copy of the subset to the results
        # if the current candidate is equal to the previous candidate continue
        # call dfs on the updated current sum and the starting index
        # return results

        res = []
        subset = []
        candidates.sort()

        def dfs(start, current_sum):
            if current_sum > target:
                return
            
            if current_sum == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                subset.append(candidates[i])
                dfs(i+1, current_sum + candidates[i])
                subset.pop()
        dfs(0,0)
        return res
            
            
# Input: candidates = [9,2,2,4,6,1,5], target = 8
# Input: candidates = [1,2,2,4,5,6,9], target = 8

# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]