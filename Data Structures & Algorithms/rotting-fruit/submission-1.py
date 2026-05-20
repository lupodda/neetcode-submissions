class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        time = 0

        def isWithinBounds(r, c):
            return 0<=r<m and 0<=c<n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh+=1

        while fresh > 0:
            flag = False
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 2:
                        for dr, dc in dirs:
                            new_r, new_c = r+dr, c+dc
                            if isWithinBounds(new_r, new_c) and grid[new_r][new_c] == 1:
                                grid[new_r][new_c] = 3
                                fresh-=1
                                flag = True

            if not flag:
                return -1

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

        return time

