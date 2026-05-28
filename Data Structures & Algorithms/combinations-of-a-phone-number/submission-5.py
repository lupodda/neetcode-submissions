class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # hashmap to convert
        # 
        digits_to_letters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []

        def backtrack(index, subset):
            if index == len(digits):
                res.append("".join(subset))# not res.append(subset.copy())
                return

            digit = digits[index]
            letters = digits_to_letters[digit]
            for l in letters:
                subset.append(l)
                backtrack(index+1, subset)
                subset.pop()

        backtrack(0,[])
        return res if digits else []


        