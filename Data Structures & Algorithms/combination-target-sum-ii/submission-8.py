class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(subset, index, current_sum):
            if current_sum > target:
                return
            
            if current_sum == target:
                res.append(subset.copy())
                return

            for start in range(index, len(candidates)):
                if start>index and candidates[start]== candidates[start-1]:
                    continue
                subset.append(candidates[start])
                backtrack(subset, start+1, current_sum+candidates[start])
                subset.pop()

        backtrack([], 0, 0)
        return res

            


            