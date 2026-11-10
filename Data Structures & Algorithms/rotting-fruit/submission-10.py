from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        total_oranges = 0
        rotten_oranges = 0
        queue = deque()
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        minutes = 0

        def is_within_bounds(i,j):
            return 0 <= i < m and 0 <= j < n 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    rotten_oranges += 1

                if grid[i][j] != 0:
                    total_oranges+=1

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
            
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if is_within_bounds(nr,nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        rotten_oranges += 1 
            if queue:
                minutes+=1

        return minutes if rotten_oranges == total_oranges else -1




        


        