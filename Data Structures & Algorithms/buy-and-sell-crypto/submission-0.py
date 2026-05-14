class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if prices == []:
            return 0

        max_profit = 0
        buy_day = 0

        for i in range(1,len(prices)):
            
            if prices[i] - prices[buy_day] > max_profit:
                max_profit = prices[i] - prices[buy_day]
                
            elif prices[buy_day] > prices[i]:
                buy_day = i
           
        return max_profit