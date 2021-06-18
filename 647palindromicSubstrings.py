class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        loop throgh and each c expand from center
        """

        pairs = [i for i in range(len(s)-1) if s[i] == s[i+1]]
        ret = len(s)+len(pairs)

        for i in range(len(s)):
            left, right = i-1, i+1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                ret += 1
                left -= 1
                right += 1
        for i in pairs:
            left, right = i-1, i+2
            while 0 <= left and right < len(s) and s[left] == s[right]:
                ret += 1
                left -= 1
                right += 1

        return ret
