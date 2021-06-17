class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = Counter(t)

        store = {}

        left, right = 0, 0

        formed = 0
        ret = float('inf'), None, None

        while right < len(s):
            c = s[right]
            if c in store:
                store[c] += 1
            else:
                store[c] = 1

            if c in target and store[c] == target[c]:
                formed += 1

            while formed == len(target) and left <= right:

                if right-left+1 < ret[0]:
                    ret = right-left+1, left, right

                store[s[left]] -= 1
                if s[left] in target and store[s[left]] < target[s[left]]:
                    formed -= 1

                left += 1
            right += 1

        return "" if ret[0] == float('inf') else s[ret[1]:ret[2]+1]
