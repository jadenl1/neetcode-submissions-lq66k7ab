class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
        
        for i in range(1, len(dp)):
            if i in coins:
                continue

            minimum = dp[i]
            for coin in coins:
                if i - coin in range(len(dp)):
                    minimum = min(minimum, dp[i - coin])
            dp[i] = minimum + 1
        
        return dp[amount] if dp[amount] != float('inf') else -1