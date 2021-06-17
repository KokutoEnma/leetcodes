class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Sliding window
        """

        if len(s) < 2:
            return min(len(s), k)

        left, ret = 0, 0
        store = {}

        for i in range(len(s)):

            if s[i] not in store:
                store[s[i]] = 1
            else:
                store[s[i]] += 1

            if i-left+1 - max(store.values()) > k:

                store[s[left]] -= 1
                left += 1
            ret = max(ret, i-left+1)

        return ret
