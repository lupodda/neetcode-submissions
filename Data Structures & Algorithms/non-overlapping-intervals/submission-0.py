class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item:item[0])
        removed_intervals = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                removed_intervals +=1
                prev_end = min(prev_end, intervals[i][1])
        return removed_intervals

        