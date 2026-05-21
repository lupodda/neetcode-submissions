class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(subset, current_sum, start):
            if current_sum > target:
                return
            
            if current_sum == target:
                res.append(subset.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(subset, current_sum+candidates[i], i+1)
                subset.pop()

        backtrack([],0,0)
        return res
        