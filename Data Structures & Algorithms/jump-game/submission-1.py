class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = dict()
        
        for i in range(n-1, -1, -1):
            for j in range(i, i + nums[i] + 1):
                if j >= n:
                    break
                if j == n-1 or (j in memo and memo[j] == True):
                    memo[i] = True
                    break
                memo[i] = False

        return memo[0]