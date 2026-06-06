class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        latest_end = intervals[0][1]
        counter = 0

        for start, end in intervals[1:]:
            if latest_end > start:
                counter+=1
            else:
                latest_end = end

        return counter
                



