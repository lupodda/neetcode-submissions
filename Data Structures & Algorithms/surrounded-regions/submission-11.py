class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len( board[0])

        directions=[(-1,0),(0,1),(1,0),(0,-1)]

        queue=deque()
        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        for r in range(m):
            if board[r][0] =="O":
                queue.append((r,0))
            if board[r][n-1] =="O":
                queue.append((r,n-1))
        for c in range(n):
            if board[0][c]=="O" :
                queue.append((0,c))
            if board[m-1][c]=="O":
                queue.append((m-1,c))



        while queue:
            r,c =queue.popleft()
            board[r][c] = "S"
            for dr, dc in directions:
                nr, nc=r+dr,c+dc
                if isWithinBounds(nr,nc) and board[nr][nc]=="O":
                    board[nr][nc]="S"
                    queue.append((nr,nc))

        for r in range(m):
            for c in range(n):
                if board[r][c]=="S":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"