class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)

        dp = [0] * (cost_len + 1)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, cost_len + 1):
            if i == cost_len:
                return min(dp[i-1], dp[i-2])
            
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
        return -1
