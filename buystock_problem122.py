class solution:
    def max_profit(self,prices):
        if not prices:
            return 0
        mn = prices[0]
        result = 0
        total_profit = 0

        for i in range(1,len(prices)):
            if prices[i] < prices[i - 1]:
                mn = prices[i]
                result = 0
                total_profit += result

            result = max(result, prices[i] - mn)
            mn = min(mn,prices[i])
        return total_profit + result