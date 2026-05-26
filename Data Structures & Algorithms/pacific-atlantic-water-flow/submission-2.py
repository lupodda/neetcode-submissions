class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        directions = [(-1,0), (0,1),(1,0),(0,-1)]

        pacific = set()
        atlantic = set()

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r,c, visited):
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            for dr, dc in directions:
                new_r, new_c = r+dr,c+dc
                if isWithinBounds(new_r, new_c) and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)
        
        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n-1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m-1, c, atlantic)

        return list(pacific & atlantic)

