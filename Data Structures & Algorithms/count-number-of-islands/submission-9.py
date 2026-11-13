class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_within_bounds(r,c):
            return 0<= r < m and 0 <= c < n

        def dfs(r,c): #fds finds all the 1s and converts them into -1s
            
            grid[r][c] = "-1"
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if is_within_bounds(nr, nc) and grid[nr][nc] == "1":
                    dfs(nr, nc)
            
        n_islands = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r,c)
                    n_islands+=1
        return n_islands
        