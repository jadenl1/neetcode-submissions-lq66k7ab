class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        minK = float('inf')
        
        while l <= r:
            k = (l + r) // 2

            # try this k
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h: # valid k
                minK = min(minK, k)
                # try slowing down
                r = k - 1
            else:
                # invalid k, we are too slow, we must speed up
                l = k + 1

        return minK
            
