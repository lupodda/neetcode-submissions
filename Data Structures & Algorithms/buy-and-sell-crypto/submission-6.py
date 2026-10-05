class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy=0

        for sell in range(len(prices)):
            max_profit=max(max_profit, prices[sell]- prices[buy])

            if prices[sell]<prices[buy]:
                buy=sell

        return max_profit
        