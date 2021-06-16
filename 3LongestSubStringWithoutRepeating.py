class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        left to store the shifting window left cursor
            when c is repeated, then try skip the gap between itself and the previous c
        record the max window size
        and record the each visited c
        """

        if len(s) < 2:
            return len(s)

        store = {}
        ret, left = 0, 0
        for i in range(len(s)):
            max_d = i
            if s[i] in store:
                left = max(left, store[s[i]])

            ret = max(ret, i-left+1)
            store[s[i]] = i+1

        return ret
