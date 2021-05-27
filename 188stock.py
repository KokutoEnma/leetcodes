class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k==0:
            return 0

        if len(prices) == 2:
            return max(0, prices[1]-prices[0])

        """
        Initialize for balance [buy, sell, buy, sell....]
        """
        dp = [0 if i%2==1 else -prices[0] for i in range(len(prices)*2)]

        for i in range(1, len(prices)):
            prev_invested = 0
            transaction = []
            for j in range(k):
                buy_ind, sell_ind = j*2, j*2+1
                buy = max(dp[buy_ind], prev_invested-prices[i])
                sell = max(dp[sell_ind], prices[i]+dp[buy_ind])
                prev_invested = sell
                transaction.append(buy)
                transaction.append(sell)
            dp = transaction
        
        return max(dp)