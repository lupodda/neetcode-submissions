class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyday = sellday =0
        profit=0

        while sellday<= len(prices) -1:
            if prices[sellday] > prices[buyday]:
                profit+=prices[sellday]-prices[buyday]
            
            buyday=sellday
            sellday+=1

        return profit