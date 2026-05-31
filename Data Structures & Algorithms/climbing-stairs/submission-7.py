class Solution:
    def climbStairs(self, n: int) -> int:
        memo  = {1:1, 2:2}
        return self._climb(n, memo)

    def _climb(self, n, memo):

        if n in memo:
            return memo[n]
        
        memo[n] = self._climb(n-1, memo) + self._climb(n-2, memo)
        return memo[n]






#          4
#   (3) 1      2 (2)
     

        