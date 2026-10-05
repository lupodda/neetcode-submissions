class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for amount in range(1, amount+1):
            for coin in coins:
                if amount-coin >= 0:
                    dp[amount] = min(1+dp[amount-coin], dp[amount])
                else:
                    break


        return dp[amount] if dp[amount]< float("inf") else -1
        