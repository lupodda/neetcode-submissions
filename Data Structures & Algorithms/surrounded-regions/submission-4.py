class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        queue = deque()

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        for r in range(m):
            if board[r][0] == "O":
                board[r][0] = "S"
                queue.append((r,0))
            if board[r][n-1] == "O":
                board[r][n-1] = "S"
                queue.append((r,n-1))

        for c in range(n):
            if board[0][c] == "O":
                board[0][c] = "S"
                queue.append((0,c))
            if board[m-1][c] == "O":
                board[m-1][c] = "S"
                queue.append((m-1,c))

        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                new_r,new_c = r+dr,c+dc
                if isWithinBounds(new_r,new_c) and board[new_r][new_c] == "O":
                    board[new_r][new_c] = "S"
                    queue.append((new_r,new_c))

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

