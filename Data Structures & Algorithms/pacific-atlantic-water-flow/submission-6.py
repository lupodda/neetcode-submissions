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
            ocean.add((r, c))
            for dr, dc in directions:
                nr,nc = r+dr, c+dc
                if is_within_bounds(nr, nc) and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc, ocean)

        for r in range(m):
            dfs(r,0, pacific_set)
            dfs(r,n-1, atlantic_set)

        for c in range(n):
            dfs(0,c, pacific_set)
            dfs(m-1,c, atlantic_set)

        valid_cells = pacific_set & atlantic_set

        return list(valid_cells)

        #MAIN TAKEAWAYS:
        # remember we can invert the thinking by starting from the cells that touch the ocean and seeing if other cells can reach it 
        # dfs is a recursive function, remember to call it inside
        # remember that we build two separate sets and then we take in intersection between them
        
        # TIME/ SPACE COMPLEXITY
        # time:  O(m*n)
        # space: O(m*n)


        

