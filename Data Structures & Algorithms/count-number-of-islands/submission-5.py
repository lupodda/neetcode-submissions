class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_islands = 0
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]

        def isWithinBounds(r, c):
            return 0 <= r < m and 0 <= c < n

        def backtrack(r,c):
            # nonlocal num_islands

            grid[r][c] = "-1"

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if isWithinBounds(nr,nc) and grid[nr][nc] == "1":
                    backtrack(nr,nc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    num_islands +=1
                    backtrack(r,c)
        return num_islands

        