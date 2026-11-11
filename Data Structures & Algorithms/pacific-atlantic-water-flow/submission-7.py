class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        directions= [(-1,0),(1,0),(0,1),(0,-1)]

        pacific = set()
        atlantic= set()

        def is_within_bounds(r,c):
            return 0<= r <m and 0<=c<n

        def dfs(r,c, ocean):
            ocean.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if is_within_bounds(nr,nc) and (nr,nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,ocean)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n-1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m-1, c, atlantic)

        return list(pacific & atlantic)
            