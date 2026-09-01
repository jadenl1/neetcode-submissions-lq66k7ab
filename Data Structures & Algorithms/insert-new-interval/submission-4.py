class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        start, end = newInterval[0], newInterval[1]
        
        i = 0
        while i < len(intervals):
            currStart, currEnd = intervals[i][0], intervals[i][1]

            if currStart > end:
                break

            overlap = (start <= currEnd and end >= currStart)
            if overlap:
                start = min(start, currStart)
                end = max(end, currEnd)
            else:
                result.append(intervals[i])
            
            i += 1
        
        result.append([start, end])

        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result