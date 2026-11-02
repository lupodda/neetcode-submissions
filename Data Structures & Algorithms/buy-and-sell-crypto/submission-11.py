class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyday=0
        maxprofit=0
        for sellday, sellprice in enumerate(prices):
            if sellprice < prices[buyday]:
                buyday=sellday
            profit=sellprice-prices[buyday]
            maxprofit=max(maxprofit, profit)

        return maxprofit