from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            dist = sqrt(((x - 0)**2) + ((y - 0)**2))
            distances.append((dist, [x,y]))

        heapq.heapify(distances)

        result = []
        while k > 0:
            result.append(heapq.heappop(distances)[1])
            k -= 1

        return result
