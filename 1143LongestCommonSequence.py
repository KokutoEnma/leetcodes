class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0]*(len(text2)+1)
        
        for i in range(len(text1)):
            temp = dp.copy()
            for j in range(len(text2)):
                if text2[j] == text1[i]:
                    dp[j+1] = temp[j]+1
                else:
                    dp[j+1]= max(dp[j], temp[j+1])
                    
        return dp[-1]