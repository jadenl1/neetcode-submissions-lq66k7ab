class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        n = len(prices)

        l = 0
        r = 0

        while r < n:
            if prices[r] >= prices[l]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            else:
                l = r
        
        return profit
