class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()
        neg_diag = set()

        res = []
        board = [["."]*n for _ in range(n)]

        def backtrack(row):

            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if row+col in pos_diag:
                    continue
                if row-col in neg_diag:
                    continue
                if col in cols:
                    continue

                cols.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                board[row][col] = "Q"

                backtrack(row+1)

                cols.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                board[row][col] = "."
                
        
        backtrack(0)
        return res

        # Time complexity: n! *n for copying
        #Space complexity: n^2 (each set stores at most n elements * at most n recursive calls)


            
                





        