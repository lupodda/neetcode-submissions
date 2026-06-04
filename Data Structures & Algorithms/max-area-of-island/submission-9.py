class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def is_withinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r, c):
            grid[r][c] = -1
            current_area = 1

            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if is_withinBounds(new_r, new_c) and grid[new_r][new_c] == 1:
                    current_area += dfs(new_r, new_c)

            return current_area


        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    island_area = dfs(r,c)
                    max_area = max(max_area, island_area)

        return max_area
        