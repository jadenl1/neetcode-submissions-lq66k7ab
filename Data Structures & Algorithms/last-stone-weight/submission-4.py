import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone

        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1

            if x == y:
                continue
            else:
                heapq.heappush(stones, abs(y - x) * -1)
        
        if stones:
            return stones[0] * -1
        
        return 0