from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0 
        minutes=0
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def is_within_bounds(r,c):
            return 0 <= r < m and 0<=c<n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c))

                if grid[r][c] == 1:
                    fresh+=1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if is_within_bounds(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        fresh-=1
                        queue.append((nr,nc))

            if queue:
                minutes+=1

        return minutes if fresh == 0 else -1

                         