from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Multi source bfs

        m = len(grid)
        n = len(grid[0])
        
        queue = deque()

        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        minutes = 0
        fresh = 0

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1

        while queue and fresh > 0: # forgot fresh >0
            minutes+=1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if isWithinBounds(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))

        return minutes if fresh == 0 else -1









