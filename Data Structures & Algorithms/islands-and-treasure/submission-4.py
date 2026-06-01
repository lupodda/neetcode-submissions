from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        land = 2147483647
        queue = deque()

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if isWithinBounds(new_r, new_c) and grid[new_r][new_c] == land:
                    grid[new_r][new_c] = 1+grid[r][c]
                    queue.append((new_r, new_c))   

        