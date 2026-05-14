from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets_rows = defaultdict(set)
        sets_columns = defaultdict(set)
        sets_boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in sets_rows[i] or
                    board[i][j] in sets_columns[j] or
                    board[i][j] in sets_boxes[i//3, j//3]):
                    return False
                sets_rows[i].add(board[i][j])                
                sets_columns[j].add(board[i][j])                
                sets_boxes[i//3, j//3].add(board[i][j])
        return True