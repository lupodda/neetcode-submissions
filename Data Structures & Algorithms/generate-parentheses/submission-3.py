class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        open_par = 0
        closed_par = 0

        def backtrack(string, open_par, closed_par):
            if open_par < closed_par or open_par > n or closed_par > n:
                return

            if open_par == closed_par == n:
                res.append("".join(string))
                return
            
            string.append("(")
            backtrack(string, open_par+1, closed_par)
            string.pop()

            string.append(")")
            backtrack(string, open_par, closed_par+1)
            string.pop()

        backtrack([], 0, 0)
        return res