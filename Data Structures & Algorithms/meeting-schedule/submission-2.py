"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n == 0 or n == 1:
            return True

        intervals.sort(key=lambda x: x.start)

        lastEnd = intervals[0].end
        for i in range(1,n):
            interval = intervals[i]
            if interval.start < lastEnd:
                return False
            lastEnd = interval.end
        
        return True