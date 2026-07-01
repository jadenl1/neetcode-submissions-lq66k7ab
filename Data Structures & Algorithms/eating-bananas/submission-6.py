class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        kMax = max(piles)
        kMin = 1

        l = kMin
        r = kMax    

        kBest = -1

        while l <= r:
            m = (l + r) // 2
            k = m # current eating rate

            # try eating rate k
            hCurr = 0
            for pile in piles:
                hCurr += math.ceil(pile/k)
            
            if hCurr <= h:
                # working k value
                kBest = k
                r = m - 1
            else:
                # k didnt work, go faster
                l = m + 1
    
        return kBest


