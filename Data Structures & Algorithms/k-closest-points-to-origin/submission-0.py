import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        # loop through points O(n)
        for x,y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            element = (-dist, [x, y])
            heapq.heappush(maxHeap, element)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        result = []
        for element in maxHeap:
            result.append(element[1])

        return result