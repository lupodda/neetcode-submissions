from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #1) create two sets, one for cells that can reach pacific and another one for cells that can reach atlantic
        #2) check the neighbors of these cells 

        m, n = len(heights), len(heights[0])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        pacific_set = set()
        atlantic_set = set()

        def is_within_bounds(r,c):
            return 0<=r<m and 0<=c<n
        
        # it takes as input the coordinates and it checks the cells i can reach (bigger one)
        def dfs(r,c, ocean):
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if is_within_bounds(nr, nc) and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                    ocean.add((nr, nc))
                    dfs(nr,nc, ocean)

        for r in range(m):
            pacific_set.add((r,0))
            atlantic_set.add((r,n-1))
            dfs(r,0, pacific_set)
            dfs(r,n-1, atlantic_set)

        for c in range(n):
            pacific_set.add((0,c))
            atlantic_set.add((m-1,c))
            dfs(0,c, pacific_set)
            dfs(m-1,c, atlantic_set)

        valid_cells = pacific_set & atlantic_set

        return list(valid_cells)



        

