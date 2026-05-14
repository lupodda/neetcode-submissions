class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(string, open_par, closed_par):
              
            if open_par == closed_par == n:
                res.append("".join(string))
                return
            
            if open_par < n:
                string.append("(")
                backtrack(string, open_par+1, closed_par)
                string.pop()

            if closed_par < open_par:
                string.append(")")
                backtrack(string, open_par, closed_par+1)
                string.pop()

        backtrack([], 0, 0)
        return res
        
            #      ""
            #      / \
            #    "("  ")"
            #    /\   /\
            #  ((  () 
            



            


  

        return res




        