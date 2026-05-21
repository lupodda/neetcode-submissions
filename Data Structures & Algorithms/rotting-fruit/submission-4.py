from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        fresh = 0
        time = 0

        def isWithinBounds(r,c):
            return 0 <= r < m and 0 <= c < n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh+=1

                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh > 0:
            length = len(queue)

            for _ in range(length):
                r,c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r+dr, c+dc
                    if isWithinBounds(new_r, new_c) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh-=1
                        queue.append((new_r, new_c))
            
            time+=1
        
        return time if fresh == 0 else -1 






        
        