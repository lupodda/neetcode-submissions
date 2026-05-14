class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            seen_nums = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_nums:
                    return False
                seen_nums.add(board[i][j])

        for j in range(n):
            seen_nums = set()        
            for i in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen_nums:
                    return False
                seen_nums.add(board[i][j])

        for square in range(n):
            seen_nums = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen_nums:
                        return False
                    seen_nums.add(board[row][col])

        return True
        
        