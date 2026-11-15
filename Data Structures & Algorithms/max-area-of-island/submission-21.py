class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def within_bounds(r,c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r,c, area):
            grid[r][c] = -1
            for dr,dc in directions:
                nr,nc, = r+dr, c+dc
                if within_bounds(nr,nc) and grid[nr][nc] == 1:
                    area = 1+dfs(nr,nc, area)

            return area

        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        max_area = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c, 1))
        return max_area

