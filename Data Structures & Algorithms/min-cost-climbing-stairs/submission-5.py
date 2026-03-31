class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp =
        # [1, 1 + 2=3, min(1 + 1, 3 + 1)=2, _, _]
        # 
        # min(cost[i] + dp[i - 1], cost[i] + dp[i - 2])
        # when we reach end, return the last value in dp
        n = len(cost)

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i-1], cost[i - 2] + dp[i-2])
        
        return dp[n]
