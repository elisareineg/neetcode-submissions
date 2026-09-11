class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = prices[0]
        maxProfit = 0
        for price in prices:
            if price < minCost:
                minCost = price
            if (price - minCost) > maxProfit:
                maxProfit = price - minCost
        return maxProfit