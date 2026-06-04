class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        pacific = set()
        atlantic = set()

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r, c, visited):
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if isWithinBounds(nr, nc) and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                    dfs(nr, nc, visited)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n-1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m-1, c, atlantic)

        return list(pacific & atlantic)

        