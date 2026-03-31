class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0]) # sort based on starting values
        result = [intervals[0]]
        lastend = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= lastend:
                lastend = max(interval[1], lastend)
                result[-1][1] = lastend
            else:
                result.append(interval)
                lastend = interval[1]
        
        return result
        
