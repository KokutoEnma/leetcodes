class Solution:
    def combinationSum4(self, N: List[int], T: int) -> int:
        """
        top down
        """
        
        dp = [0] * (T+1)
        dp[0] = 1
        
        for i in range(1, T+1):
            for n in N:
                if n<=i:dp[i]+=dp[i-n]
        return dp[-1]
        
        """
        bottom up
        """
#         dp = [0] * (T+1)
#         dp[0] = 1
        
#         for i in range(T):
#             # if not dp[i]:continue
#             for n in N:
#                 if n+i<=T: dp[i+n] += dp[i]
#         return dp[-1]
                    
        