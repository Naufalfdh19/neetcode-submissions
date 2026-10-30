class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = prices[0]

        for i in range(len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                if maxProfit < prices[i]-buy:
                    maxProfit = prices[i]-buy
        
        return maxProfit
