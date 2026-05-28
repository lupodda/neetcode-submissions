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

        #TAKEWAYS:
        # remember to join the elements in subset
        # when building a data structure we have to use it, I was not using digits_to_letters
        # check edge cases like empty string as input

        #Time complexity: n = nuber of digits m braching factor = max(length of each group) -> n* m^n
        # Space complexity: n


        