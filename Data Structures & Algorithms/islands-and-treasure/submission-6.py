from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        treasure = 0
        water = -1 
        distance = 1

        m, n = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        queue = deque()

        def is_within_bounds(r,c):
            return 0<=r<m and 0<=c<n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == treasure:
                    queue.append((r,c))

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if is_within_bounds(nr,nc) and grid[nr][nc] == land:
                    grid[nr][nc] = grid[r][c]+1
                    queue.append((nr,nc))

