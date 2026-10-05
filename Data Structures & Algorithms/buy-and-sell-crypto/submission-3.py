class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy_time=0
        for sell_time, price in enumerate(prices):
            current_profit= price-prices[buy_time]
            max_profit=max(max_profit, current_profit)
            if price<prices[buy_time]:
                buy_time=sell_time

        return max_profit
        