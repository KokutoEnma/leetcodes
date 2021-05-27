class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        if len(prices) == 2:
            return max(0, prices[1]-prices[0])

        """
        Initialize for balance
        """
        dp = [-prices[0], 0, -prices[0], 0]

        for i in range(1, len(prices)):

            buy1 = max(dp[0], -prices[i])
            sell1 = max(dp[1], prices[i]+dp[0])

            buy2 = max(dp[2], sell1-prices[i])
            sell2 = max(dp[3], prices[i]+dp[2])
            dp = [buy1, sell1, buy2, sell2]

        return max(dp)

        # dp[0] hold from 1st transaction
        # dp[1] sold from 1st transaction
        # dp[2] hold from 2st transaction
        # dp[3] sold from 2nd transaction

#         if len(prices)<1:
#             return 0

#         # initialize dp
#         dp=[-prices[0], 0, -prices[0], 0]
#         for i in range(1, len(prices)):
#             curr = dp.copy()
#             curr[0] = max(-prices[i], dp[0])
#             curr[1] = max(dp[0] + prices[i], dp[1])
#             curr[2] = max(dp[1] - prices[i], dp[2])
#             curr[3] = max(dp[2] + prices[i], dp[3])
#             dp = curr.copy()
#         return max(dp)

        """
        FAILED ATTEMPT
        """

#         def getMaxProfit(ps):
#             ret = 0
#             mn = ps[0]
#             for p in ps:
#                 if p < mn:
#                     mn = p
#                 else:
#                     ret = max(ret, p-mn)
#             return ret

#         single_trans = getMaxProfit(prices)

#         prev_top_ind = 0
#         prev_bot_ind = 0
#         max_diff_top_ind = 0
#         max_diff_bot_ind = 0
#         max_diff = 0
#         for i in range(len(prices)):
#             if prices[i] >= prices[prev_top_ind]:
#                 prev_top_ind = i
#             else:
#                 prev_bot_ind = i
#             diff = prices[prev_top_ind] - prices[prev_bot_ind]
#             if diff>max_diff:
#                 max_diff = diff
#                 max_diff_top_ind = prev_top_ind
#                 max_diff_bot_ind = prev_bot_ind

#         print(max_diff_top_ind, max_diff_bot_ind)
#         print(getMaxProfit(prices[:max_diff_top_ind+1]), getMaxProfit(prices[max_diff_bot_ind:]))
#         print(prices[:max_diff_top_ind+1])

#         if max_diff_top_ind==0 or max_diff_bot_ind==0:
#             return single_trans
#         if max_diff_top_ind+1 == len(prices):
#             return single_trans

#         double_trans = getMaxProfit(prices[:max_diff_top_ind+1])+getMaxProfit(prices[max_diff_bot_ind:])


#         return max(single_trans, double_trans)
