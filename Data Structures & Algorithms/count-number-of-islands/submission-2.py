class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        n_islands = 0

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r, c):
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "-1"

            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if isWithinBounds(new_r, new_c) and grid[new_r][new_c] == "1":
                    dfs(new_r, new_c)    

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    n_islands +=1
                    dfs(r,c)

        return n_islands
                
                        




        