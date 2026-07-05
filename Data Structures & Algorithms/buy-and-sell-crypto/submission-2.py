class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) # 6

        profit = 0

        i = 0
        while i < n:
            j = i
            while j < n and prices[j] >= prices[i]:
                profit = max(profit, prices[j] - prices[i])
                j += 1
                
            if i == j:
                i += 1
            else:
                i = j

        return profit