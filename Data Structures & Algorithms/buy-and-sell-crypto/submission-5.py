class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        n = len(prices)

        result = 0

        while r < n:
            while r in range(n) and l in range(n) and prices[r] >= prices[l]:
                result = max(result, prices[r] - prices[l])
                r += 1
            l = r
            r += 1

        return result