class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def backtrack(start, current_sum):
            if current_sum == target:
                res.append(subset.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if current_sum + candidates[i] > target:
                    break

                subset.append(candidates[i])
                backtrack(i+1, current_sum + candidates[i])
                subset.pop()

        backtrack(0,0)
        return res

            

        