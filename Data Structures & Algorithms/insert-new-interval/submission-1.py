class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        left, right = 0, n-1
        target = newInterval[0]
        
        while left <= right:
            mid = (left+right)//2

            if intervals[mid][0] < target:
                left = mid+1
            else:
                right = mid-1

        intervals.insert(left, newInterval)
        res = [intervals[0]]

        for start, end in intervals[1:]:
            latest_end =res[-1][1]
            if start <= latest_end:
                res[-1][1] = max(latest_end, end)
            else:
                res.append([start, end])

        return res
                

            
            
            