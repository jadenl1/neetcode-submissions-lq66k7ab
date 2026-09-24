class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = max(piles)

        while l <= r:
            k = (l + r) // 2
            
            # try this k
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                minK = min(minK, k)
                r = k - 1
            else:
                l = k + 1
        
        return minK