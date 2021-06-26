class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        topdown iterative
        """
        ns = len(s)
        np = len(p)

        dp = [[False]*(np+1) for _ in range(ns+1)]

        dp[0][0] = True

        for i in range(1, np+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        for i in range(1, ns+1):
            for j in range(1, np+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[-1][-1]

        """
        bottom up
        """

#         dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]

#         # the last one s="" p="" is always true


#         dp[-1][-1]=True


#         for i in range(len(s), -1, -1):
#             for j in range(len(p)-1, -1, -1):
#                 first_match = i<len(s) and p[j] in {s[i], '.'}

#                 if j+1<len(p) and p[j+1] == '*':
#                     dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
#                 else:
#                     dp[i][j] = first_match and dp[i+1][j+1]

#         return dp[0][0]

        """
        top down 
        recursion topdown
        """

#         dp = {}

#         def check(i, j):
#             if (i,j) not in dp:
#                 if j==len(p):
#                     dp[i,j] = i==len(s)
#                 else:
#                     first_match = i<len(s) and p[j] in {s[i], '.'}

#                     if j+1<len(p) and p[j+1]=='*':
#                         dp[i,j]=check(i, j+2) or first_match and check(i+1, j)
#                     else:
#                         dp[i,j]=first_match and check(i+1, j+1)


#             return dp[i,j]

#         return check(0, 0)
