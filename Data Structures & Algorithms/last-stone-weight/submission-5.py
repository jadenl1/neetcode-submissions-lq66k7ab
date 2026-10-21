import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1

            if x == y:
                continue
            elif x < y or y < x:
                z = max(x, y) - min(x, y)
                heapq.heappush(stones, -z)
        
        return -stones[0] if len(stones) == 1 else 0


