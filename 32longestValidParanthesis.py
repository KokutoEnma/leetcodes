class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        dynamic programming

        dp[i] -> length of longest substring ending at i
        init 0
        only ending ) is valid and ending ( is always 0
        1. check each 2 if consective as ( and )
        2. when )): dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2

        """
#         if len(s)<1: return 0

#         dp = [0]*len(s)

#         for i in range(1, len(s)):
#             if s[i] == ')':
#                 if s[i-1] == '(':
#                     dp[i] = 2 if i<2 else 2+dp[i-2]
#                 elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
#                     dp[i] = dp[i-1] + (2 if i-dp[i-1]<2 else dp[i-dp[i-1]-2]+2)

#         return max(dp)

        """
        stack
        push when (
        pop when ), longest length -> i-last stack item
        """
#         stack = [-1]
#         ret = 0

#         for i in range(len(s)):
#             if s[i] == '(': stack.append(i)
#             else:
#                 stack.pop()
#                 if not stack: stack.append(i)
#                 else: ret = max(ret, i-stack[-1])

#         return ret

        """
        forward check for counting (, when #( == #) take max 2*#)
        backward check for counting ), when #( == #) tack max 2*#(
        else #(=#)=0
        """
        left = right = ret = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ret = max(ret, 2*right)
            elif right >= left:
                left = right = 0
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ret = max(ret, 2*left)
            elif left >= right:
                left = right = 0

        return ret
