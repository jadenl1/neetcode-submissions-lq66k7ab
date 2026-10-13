"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []  # list of tups: (time, isStart)

        for interval in intervals:
            times.append((interval.start, True))
            times.append((interval.end, False))
        
        times.sort(key=lambda x: (x[0], x[1]))

        result = 0
        count = 0
        for time, isStart in times:
            if isStart:
                count += 1
            else:
                count -= 1
            result = max(result, count)
        
        return result
