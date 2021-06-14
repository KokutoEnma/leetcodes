class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        """
        pick which ends first, this is a greedy problem---get as much time intervals as possible
        """

        non_merged = []
        for interval in intervals:

            if not non_merged or non_merged[-1][1] <= interval[0]:
                non_merged.append(interval)

            elif interval[1] < non_merged[-1][1]:
                non_merged.pop()
                non_merged.append(interval)

        return len(intervals) - len(non_merged)
