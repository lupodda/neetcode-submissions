class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        n = len(board)
        m = len(board[0])

        def backtrack(index, row, col):

            if index == len(word):
                return True
            
            if row < 0 or row >= n or col < 0 or col >= m:
                return False

            if board[row][col] == "#":
                return False
            
            if board[row][col] != word[index]:
                return False
            
            board[row][col] = "#"
            res = False
            for dir_row, dir_col in directions:
                new_dir_r = dir_row + row
                new_dir_c = dir_col + col
                res |= backtrack(index+1, new_dir_r, new_dir_c)
                
            board[row][col] = word[index]
            return res

        for row in range(n):
            for col in range(m):
                if backtrack(0, row, col):
                    return True
        return False

        #time and space complexity:
        # time: n*m * 3^l -> l=len of word
        # space: l -> recursion stack


            

                


            
        
        