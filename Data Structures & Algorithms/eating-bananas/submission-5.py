class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # given eating rate k, we can determine that at a pile w/ i bananas:
            # we eat that pile in math.ceil(i/k) hours

        #ex. [1, 4, 3, 2, 5] h=9
        # k-list (all possible values of k):
            # ex. [1, 2, 3, 4, 5] <- min to max in input
        
        n = len(piles)
        l = 1
        r = max(piles)

        bestK = 0

        while l <= r:
            k = (l + r) // 2

            currH = 0
            for i in range(n):
                currH += math.ceil(piles[i]/k)

            if currH <= h:
                r = k - 1
                bestK = k
            elif currH > h:
                l = k + 1

        return bestK

        # ex. [1, 3, 4, 5, 7] h=10

        # allK [1, 2, 3, 4, 5, 6, 7]

        # @ k=4, 7 hours


        # binary search, go to mid (k=3)
            # try input with k=3 -> 1 + 1 + 1 + 2 + 2 = 7 hours
            # since we do k=3 in 7 hours (h=9), we can actually increase k while staying under the total hours h=9
            # move k right
    
    #[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        