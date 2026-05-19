class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        dirs=[(-1,0),(0,1),(1,0),(0,-1)]
        max_area=0

        def isWithinBounds(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        
        def dfs(r,c, area):
            grid[r][c]=-1
            for d in dirs:
                new_r,new_c = r+d[0], c+d[1]
                if isWithinBounds(new_r, new_c) and grid[new_r][new_c]==1:
                    area=dfs(new_r,new_c, area+1)
            return area



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] ==1:
                    area=dfs(r,c, 1)
                    max_area=max(max_area, area)
        return max_area
        