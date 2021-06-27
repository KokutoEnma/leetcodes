class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        """
        bottom up
        """
        
#         dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        
#         dp[-1][-1] = True
        
#         for i in range(len(p)-1, -1, -1):
#             if p[i]=='*': dp[-1][i] = dp[-1][i+1]
        
#         for i in range(len(s)-1, -1, -1):
#             for j in range(len(p)-1, -1, -1):
#                 if p[j]=='?':
#                     dp[i][j] = dp[i+1][j+1]
#                 elif p[j]=='*':
#                     dp[i][j] = dp[i+1][j] or dp[i][j+1]
#                 elif s[i]==p[j]:
#                     dp[i][j] = dp[i+1][j+1]
        
#         return dp[0][0]

        """
        top down
        """
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        
        for i in range(len(p)+1):
            if i>0 and p[i-1]=='*': dp[0][i] = dp[0][i-1]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                
                if p[j-1] =='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]