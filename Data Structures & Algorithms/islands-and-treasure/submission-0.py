from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1,0), (0,1), (0,-1), (1,0)]
        land = 2147483647
        m = len(grid)
        n = len(grid[0])
        distance = 0
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))

        def is_within_bounds(r,c):
            return 0 <= r < m and 0 <= c < n

        while queue:
            r,c = queue.popleft()
            
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if is_within_bounds(new_r, new_c) and grid[new_r][new_c] == land:
                    grid[new_r][new_c] = grid[r][c]+1
                    queue.append((new_r,new_c))
                

                









#  [[L,W,T,L],  
#   [L,L,L,W],
#   [L,W,L,W],
#   [T,W,L,L]]

