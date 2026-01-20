class solution:
    def  max_profit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0,0] for _ in range(n)]

        mn = prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], prices[i] - mn)
            mn = min(mn, prices[i])

        mx = prices[-1]
        for i in range(n-2,-1,-1):
            dp[i][1] = max(dp[i+1][1],dp[i][0] + mx - prices[i])
            mx = max(mx, prices[i])

        return max(dp[-1][0], dp[0][1])