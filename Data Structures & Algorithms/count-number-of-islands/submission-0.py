class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n_islands = 0

        def is_within_bounds(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) 

        def dfs(r, c):
            grid[r][c] = "-1"
            for d in directions:
                new_r, new_c = r+d[0], c+d[1]
                if is_within_bounds(new_r, new_c) and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)                        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    n_islands += 1

        return n_islands


        