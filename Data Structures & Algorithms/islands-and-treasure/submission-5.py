from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1,0), (0,1),(1,0),(0,-1)]
        land = 2147483647
        queue = deque()

        def isWithinBounds(r,c):
            return 0 <= r < m and 0 <= c < n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            r,c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if isWithinBounds(nr, nc) and grid[nr][nc] == land:
                    grid[nr][nc] = 1+grid[r][c]
                    queue.append((nr,nc))



