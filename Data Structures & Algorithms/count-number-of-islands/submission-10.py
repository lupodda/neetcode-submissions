class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            grid[r][c]="-1"
            for dr, dc in directions:
                nr, nc= r+dr,c+dc
                if 0<=nr<m and 0<= nc< n and grid[nr][nc]=="1":
                    dfs(nr,nc)
        m=len(grid)
        n=len(grid[0])
        total=0
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] =="1":
                    dfs(r,c)
                    total+=1

        return total
