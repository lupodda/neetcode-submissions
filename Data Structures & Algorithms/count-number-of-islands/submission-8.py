class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate trough all the rows and columns
        # if the element in the grid is 1 then increment the n of islands and call dfs
        # inside dfs madify in place the curent element
        # check all the neighbors of the current elements, if it's a 1 call dfs

        m = len(grid)
        n = len(grid[0])
        n_islands = 0
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r,c):
            grid[r][c] = "-1"

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if isWithinBounds(nr, nc) and grid[nr][nc] == "1":
                    dfs(nr, nc)


        for r in range(m):
            for c in range(n):
                if grid[r][c] =="1":
                    n_islands+=1
                    dfs(r,c)

        return n_islands
