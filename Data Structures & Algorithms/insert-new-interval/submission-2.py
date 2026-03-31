class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        result = []

        # linear loop through all intervals
        for i, currInterval in enumerate(intervals):
            # case 1: newInterval comes before curr interval
            # end of newInterval < start of curr interval
            if newInterval[1] < currInterval[0]:
                result.append(newInterval)
                # once we place our new interval we can just return the rest of list after
                return result + intervals[i:]
            # case 2: newInterval comes after curr interval
            elif newInterval[0] > currInterval[1]:
                result.append(currInterval)
            # case 3: otherwise, there must be some overlap 
            else:
                newInterval = [min(newInterval[0], currInterval[0]), max(newInterval[1], currInterval[1])]
        
        result.append(newInterval)

        return result

