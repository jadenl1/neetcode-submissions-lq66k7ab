"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        # sort everything first by start value
        intervals.sort(key=lambda x: x.start)
        
        # the moment we find an overlap, we return False
        for i in range(len(intervals) - 1):
            # if at any interval, the next intervals start is < current end, there is an overlap
            thisInterval = intervals[i]
            nextInterval = intervals[i + 1]

            if nextInterval.start < thisInterval.end:
                return False

        return True
        # if we get through the entire list without any overlaps, then return True