"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        active_events = 0
        meeting_rooms = 0
        for interval in intervals:
            events.append((interval.start, "S"))
            events.append((interval.end, "E"))

        events.sort()
        
        for event in events:
            if event[1] == "S":
                active_events +=1
                meeting_rooms = max(meeting_rooms, active_events)
            else:
                active_events -=1

        return meeting_rooms

        
            

        