from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #         if len(intervals)<2: return intervals

        #         intervals.sort()

        #         ret = [intervals[0]]
        #         for i in range(1, len(intervals)):
        #             if intervals[i][1]>=ret[-1][0] and intervals[i][1]<= ret[-1][1] or intervals[i][0]>=ret[-1][0] and intervals[i][0] <= ret[-1][1] or intervals[i][0]<=ret[-1][0] and intervals[i][1]>=ret[-1][1]:
        #                 ret[-1] = [min(ret[-1][0], intervals[i][0]), max(ret[-1][1], intervals[i][1])]
        #             else:
        #                 ret.append(intervals[i])

        #         return ret

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
