class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = list(range(n+1))

        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
        