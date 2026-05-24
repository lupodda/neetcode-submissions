from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        queue = deque()

        for r in range(m):
            if board[r][0] == "O":
                queue.append((r,0))
            if board[r][n-1] == "O":
                queue.append((r,n-1))

        for c in range(n):
            if board[0][c] == "O":
                queue.append((0,c))
            if board[m-1][c] == "O":
                queue.append((m-1,c))

        while queue:
            r, c = queue.popleft()
            board[r][c] = "S"
            
            for dr,dc in directions:
                new_r, new_c = r+dr, c+dc
                if isWithinBounds(new_r,new_c) and board[new_r][new_c] == "O":
                    board[new_r][new_c] = "S"
                    queue.append((new_r,new_c))

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

    #MAIN TAKEAWAYS:
    # when I am stuck in a solution try to think with a reversed approach
    # We can store intermediate results to avoid increasing the space complexity
    # processing some cells at the begining by modifying them in place is the trick
    # do a final pass to align the preprocessed board to the output

    # Time complexity: O(n*m)
    # Space complexity: O(n*m)









