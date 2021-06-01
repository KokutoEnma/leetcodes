class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        forward
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                if s[i:j] in wordDict and dp[i]:
                    dp[j] = True
        
        return dp[-1]
        
        
        
        """
        initial backward, slow
        """
        
#         dp = [0]*(len(s)+1)
        
#         for i in range(len(s)):
#             for j in range(i, -1, -1):
#                 if s[j:i+1] in wordDict:
#                     dp[i+1] = max(dp[j] + i-j+1, dp[i+1])
                                
#         return dp[-1] == len(s)
            
        """
        backward
        """
        
#         dp = [False]*(len(s)+1)
#         dp[0] = True
                
#         for i in range(len(s)+1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in wordDict:
#                     dp[i] = True
#                     break
        
#         return dp[-1]

        
        
        