class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        def isWithinBounds(r,c):
            return 0<=r<m and 0<=c<n

        def backtrack(r,c, index):
            if index == len(word):
                return True

            if not isWithinBounds(r,c):
                return False
            
            if board[r][c] != word[index]:
                return False
            
            if board[r][c] == "#":
                return False

            board[r][c] = "#"
            flag = False
            for dr,dc in directions:
                new_r, new_c = r+dr, c+dc
                flag |= backtrack(new_r, new_c, index+1)

            board[r][c] = word[index]
            
            return flag

        for r in range(m):
            for c in range(n):
                if backtrack(r,c,0):
                    return True

        return False


        