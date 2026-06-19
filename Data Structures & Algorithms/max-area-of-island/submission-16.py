class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_area=0

        dirs=[(-1,0),(0,1),(1,0),(0,-1)]
        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r,c,area):
            grid[r][c]=-1
            for dr,dc in dirs:
                nr, nc =r+dr, c+dc
                if isWithinBounds(nr, nc) and grid[nr][nc]==1:
                    area= dfs(nr,nc,area+1)

            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    max_area=max(max_area, dfs(r,c,1))

        return max_area
