class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            start, end = interval
            new_start, new_end = newInterval

            if new_end < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < new_start:
                res.append(interval)
            else:
                newInterval[0] = min(start, new_start)
                newInterval[1] = max(end, new_end)

        res.append(newInterval)
        return res