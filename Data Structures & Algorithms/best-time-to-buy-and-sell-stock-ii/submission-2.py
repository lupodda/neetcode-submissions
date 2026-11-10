class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = sell_day = 0
        profit = 0
        while sell_day <= len(prices)-1:
            if prices[sell_day] > prices[buy_day]:
                profit += prices[sell_day] - prices[buy_day]
            
            buy_day = sell_day
            sell_day+=1

        return profit

        