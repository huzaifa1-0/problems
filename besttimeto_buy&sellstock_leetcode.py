class Solution(object):
    def maxProfit(self, prices):
        mn = prices[0]
        result = 0
        for price in prices:
            result = max(result, price - mn)
            mn = min(mn, price)
        return result