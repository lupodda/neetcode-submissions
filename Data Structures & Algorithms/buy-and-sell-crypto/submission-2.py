class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through the array with two pointers starting from the beginning
        # use two pointers buy_day and sell_day
        # update the profit if thenew profit is bigger
        # update the buy day if the current day is cheaper than the previous


        max_profit = 0
        buy_day = 0
        for i in range(len(prices)):
            current_profit = prices[i]-prices[buy_day]
            max_profit = max(max_profit, current_profit)

            if prices[i]< prices[buy_day]:
                buy_day = i
        
        return max_profit
        