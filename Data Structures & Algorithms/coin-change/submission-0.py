from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amount):
            if amount == 0:
                return 0
            
            res = float("inf")

            for coin in coins:
                if amount-coin >= 0:
                    res = min(res, 1+dfs(amount-coin))
            return res
        coins_needed = dfs(amount)
        return coins_needed if coins_needed < float("inf") else -1
        