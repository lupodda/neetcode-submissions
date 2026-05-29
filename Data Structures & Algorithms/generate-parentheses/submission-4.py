class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(n_open, n_closed, subset):
            if n_open < n_closed:
                return

            if n_open == n_closed == n:
                res.append("".join(subset))
                return

            if n_open < n:
                subset.append("(")
                backtrack(n_open+1, n_closed, subset)
                subset.pop()

            if n_closed < n_open:
                subset.append(")")
                backtrack(n_open, n_closed+1, subset)
                subset.pop()

        backtrack(0,0, [])
        return res


            

            
            





        