import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heapify stones
        maxHeap = []
        for i, weight in enumerate(stones):
            maxHeap.append(-weight)
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -(heapq.heappop(maxHeap))
            y = -(heapq.heappop(maxHeap))

            if x == y:
                continue
            if x < y:
                result = y - x
                heapq.heappush(maxHeap, -result)
            if y < x:
                result = x - y
                heapq.heappush(maxHeap, -result)
        
        if len(maxHeap) == 1:
            return -maxHeap[0]
        return 0