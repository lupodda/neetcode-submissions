class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if prices == []:
            return 0

        max_profit = 0
        buy_day = 0

        for i in range(1, len(prices)):
            current_profit = prices[i] - prices[buy_day]
            if current_profit > max_profit:
                max_profit = current_profit

            elif prices[i] < prices[buy_day]:
                buy_day = i
            
        return max_profit

            
        