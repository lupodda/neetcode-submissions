class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals: 
            latest_end = res[-1][1]

            if start <= latest_end:
                res[-1][1] = max(end, latest_end)
            else:
                res.append([start, end])
        return res

            

        