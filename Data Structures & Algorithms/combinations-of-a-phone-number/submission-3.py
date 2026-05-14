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

        def backtrack(string, index):

            if len(string) == len(digits):
                res.append("".join(string))
                return
            
            for letter in digit_to_letter[digits[index]]:
                string.append(letter)
                backtrack(string, index+1)
                string.pop()

        if digits:
            backtrack([], 0)
        return res

        # TIME AND SPACE COMPLEXITY
        # time n*4^n
        #space n

        #MAIN TAKEWAYS
        # convert numbers to string in a dict
        # handle the case where no digits are passed
        # use the index of digits rather than the letter itself






        


        
        