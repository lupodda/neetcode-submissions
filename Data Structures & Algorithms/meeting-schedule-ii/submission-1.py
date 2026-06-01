"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = []
        counter = 0
        meeting_rooms = 0

        for interval in intervals:
            meetings.append((interval.start, "S"))
            meetings.append((interval.end, "E"))

        meetings.sort()

        for meeting_time, meeting_type in meetings:
            if meeting_type == "S":
                counter +=1
                meeting_rooms = max(meeting_rooms, counter)
            else:
                counter-=1

        return meeting_rooms




        