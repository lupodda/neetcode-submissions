class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n =len(nums)
        res=[]


        def backtrack(start, subset):
            res.append(subset.copy())
            
            for i in range(start, n):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        backtrack(0,[])
        return res