class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def dfs(start, subset):
            res.append(subset.copy())

            for i in range(start,n):
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()

        dfs(0,[])
        return res
