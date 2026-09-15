import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ORIGIN = 0
        max_heap = []

        for x, y in points:
            dist = math.sqrt( ((x - ORIGIN) ** 2) + ((y - ORIGIN) ** 2) )
            
            heapq.heappush(max_heap, [-dist, x, y])

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        result = []
        for dist, x, y in max_heap:
            result.append([x,y])

        return result