class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter ={"2":"abc",
                           "3":"def",
                           "4":"ghi",
                           "5":"jkl",
                           "6":"mno",
                           "7":"pqrs",
                           "8":"tuv",
                           "9":"wxyz"}

        res = []
        
        if len(digits) == 0:
            return res

        def backtrack(string, index):


            if len(string) == len(digits):
                res.append("".join(string))
                return
            
            for letter in digit_to_letter[digits[index]]:
                string.append(letter)
                backtrack(string, index+1)
                string.pop()

        backtrack([], 0)
        return res





        


        
        