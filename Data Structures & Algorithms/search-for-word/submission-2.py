class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # at each step check the neighbours and see if the current char in the target word is a neighbour
        # so at each step I am choosing among the neighbours

        def backtrack(index, row, col):
            if index == len(word):
                return True
            
            if (row >= m or col >= n) or (row < 0 or col < 0):
                return False
                
            if board[row][col] != word[index]:
                return False

            if board[row][col] == "#":
                return False

            board[row][col] = "#"
            flag = False

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                flag = flag or backtrack(index+1, nr, nc)
                
            board[row][col] = word[index]
            return flag

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(0, row, col):
                    return True

        return False
            
            # check the current element in the board, if it's equal to the current char in the word return true
            # check the neighbouring elements, if they are equal to the index+1 char return true

            # MAIN TAKEAWAYS
            # lots of base cases -> analyze all the corner cases
            # ovrwrite the seen chars with # to avoid revisiting the same cell
            # 
            
            



            


            
            
            
            




        
        