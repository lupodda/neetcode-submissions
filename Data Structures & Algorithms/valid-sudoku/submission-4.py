class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        for r in range(m):
            seen = set()
            for c in range(n):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        for c in range(n):
            seen = set()
            for r in range(m):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])


        for square in range(9):
            seen = set()

            for r in range(3):
                for c in range(3):
                    row = (square//3)*3+r
                    col = (square%3)*3+c

                    if board[row][col] == ".":
                        continue
                
                    if board[row][col] in seen:
                        return False

                    seen.add(board[row][col])


        return True


                
        

        