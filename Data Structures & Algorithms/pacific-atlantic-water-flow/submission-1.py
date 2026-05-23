class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        def isWithinBounds(r,c):
            return (0<=r<m and 0 <= c < n)

        def dfs(r, c, visited):
            if (r,c) in visited:
                return

            visited.add((r,c))
            for dr,dc in directions:
                new_r, new_c = r+dr, c+dc
                if isWithinBounds(new_r,new_c) and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)
            
        for c in range(n):
            dfs(0,c,pacific)
            dfs(m-1,c,atlantic)

        for r in range(m):
            dfs(r,0, pacific)
            dfs(r,n-1, atlantic)

        return list(pacific & atlantic)
        
        # MAIN TAKEAWAYS
        # try to use reverse thinking to go from the solution to the beginning
        # remember to store visited cells and if we aready visited return directly
        # when returning we already have all the visited cells. take the intersection between sets
        # Always check the boundaries first in the condition for all the indexes


        