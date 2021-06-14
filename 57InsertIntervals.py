class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)<1: return [newInterval]
        start, end = newInterval

        ret = []
        i=0
        while i<len(intervals):
            s, e = intervals[i]
            if start>e:
                ret.append([s, e])
            elif end>=s and end<=e or start>=s and end<=e or start>=s and start<=e:
                start = min(start, s)
                end = max(end, e)
            elif end<s:
                break
            i+=1

        return ret+[[start, end]]+ intervals[i:]