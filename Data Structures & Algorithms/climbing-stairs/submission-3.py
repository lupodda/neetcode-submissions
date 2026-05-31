from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climb(n)

    @cache
    def _climb(self, n):
        if n <= 2:
            return n
        return self._climb(n-1) + self._climb(n-2)






#          4
#   (3) 1      2 (2)
     

        