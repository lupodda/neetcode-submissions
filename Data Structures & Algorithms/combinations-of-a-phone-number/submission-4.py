class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        

        def backtrack(subset, index):
            if index == len(digits):
                res.append("".join(subset))
                return
            
            for letter in digit_to_letters[digits[index]]:
                subset.append(letter)
                backtrack(subset, index+1)
                subset.pop()
                
        if digits:
            backtrack([], 0) 
        return res